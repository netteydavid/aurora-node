class Decidable:
    def __init__(self, id):
        self.ID = id
        self.accepted = False
        self.rejected = False
    
    def Accept(self):
        self.accepted = True
        self.rejected = False

    def Reject(self):
        self.accepted = False
        self.rejected = True

    def Status(self):
        if self.accepted:
            return "accepted"
        elif self.rejected:
            return "rejected"
        else:
            return "none"