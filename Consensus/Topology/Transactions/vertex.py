import uuid
from ..decidable import Decidable
from ...constants import Status
#TODO: Redo this with information from developer docs
class Vertex(Decidable):
    def __init__(self, parents, chit, txs):
        self.parents = parents
        self.chit = chit
        self.transactions = txs
        #TODO: Merkle Tree
        #TODO: Get ID, generate or pass in?
        self.confidence = 0
        self.successes = 0
        if chit:
            self.confidence = 1
            self.successes = 1
        super().__init__()

    def IsPreferred(self):
        result = True
        for tx in self.transactions:
            result = result and tx.IsPreferred()
        return result

    def IsStronglyPreferred(self):
        #status is none, determine if strongly preferred
        retVal = self.IsPreferred()
        for parent in self.parents:
            #Check if ancestors are strongly preferred as well
            retVal = retVal and parent.IsStronglyPreferred()
        return retVal
    
    def IsAccepted(self, beta1, beta2):
        # Check if status has already been changed
        if self.status == Status.accepted:
            return True
        elif self.status == Status.rejected:
            return False
        
        # Safe early commitment
        result = self.IsVirtuous()
        for parent in self.parents:
            result = result and parent.IsAccepted(beta1, beta2)
        result = result and self.confidence >= beta1

        # Check consecutive counter
        result = result or self.successes >= beta2

        # If it is accepted, change status to accepted
        if result:
            self.Accept()

        return result

    def IsVirtuous(self):
        result = True
        for tx in self.transactions:
            result = result and tx.virtuous
        return result

    