
class Output:
    def __init__(self, value, lock, lockSize):
        # Amount in satoshis (hex)
        self.value = value
        # Locking script (hex)
        self.lock = lock
        # Lock size (hex)
        self.locksize = lockSize

    def Unlock(self, script):
        #TODO: Parse script and use it to unlock the lock
        return True
    