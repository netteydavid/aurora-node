import decidable as d

#TODO: Look at vertex.go, input.go, and tx.go
#TODO: Vertex optimization

class Output(d.Decidable):
    def __init__(self, id, parents, chit):
        self.parents = parents
        self.chit = chit
        self.confidence = 0
        self.successes = 0
        if chit:
            self.confidence = 1
            self.successes = 1
        super().__init__(id)
        self.conflictSet = id
        self.virtuous = True

    def IsPreferred(self):
        return self.conflictSet == self.ID

    def IsStronglyPreferred(self):
        retVal = self.IsPreferred()
        for parent in self.parents:
            #Check if ancestors are strongly preferred as well
            retVal = retVal and parent.IsStronglyPreferred()
        return retVal
    
    def IsAccepted(self, beta1, beta2):
        retVal = self.confidence >= beta1 and self.virtuous
        for parent in self.parents:
            retVal = retVal and parent.IsAccepted(beta1, beta2)
        retVal = retVal or self.confidence >= beta2
        return retVal

    def SetConflictLeader(self, leader):
        self.conflictSet = leader
        self.virtuous = self.IsPreferred()