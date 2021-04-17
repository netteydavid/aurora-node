from ..constants import Status
class Decidable:
    def __init__(self):
        self.accepted = False
        self.rejected = False
        self.status = Status.none
    
    def Accept(self):
        self.accepted = True
        self.rejected = False

    def Reject(self):
        self.accepted = False
        self.rejected = True

    def SetStatus(self):
        if self.accepted:
            self.status = Status.accepted
        elif self.rejected:
            self.status = Status.rejected
        else:
            self.status = Status.none