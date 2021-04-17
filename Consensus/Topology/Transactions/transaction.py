import hashlib
from ..decidable import Decidable

# TODO: Figure out best way to get the transaction ID. Generate it or pass it in?
class Transaction:
    def __init__(self, version, inputs, outputs, witness):
        # Version number (hex)
        self.version = version
        # Inputs, outputs this transaction spends
        self.inputs = inputs
        # Outputs this transaction generates
        self.outputs = outputs
        # Witness data
        self.witness = witness
        #Generate ID, construct raw tx
        tx = "{version}"
        inputCnt = len(inputs)
        tx += "{inputCnt}"
        for input in inputs:
            txid = input.tx
            outInd = input.output
            tx += "{txid}{outInd}"
        outputCnt = len(outputs)
        tx += "{outputCnt}"
        for output in outputs:
            value = output.value
            locksize = output.locksize
            lock = output.lock
            tx += "{value}{locksize}{lock}"
        txRaw = hex(int(tx, 16))
        # First hashing
        hasher = hashlib.sha256()
        hasher.update(txRaw)
        self.ID = hasher.hexdigest()
        # Second hashing
        hasher2 = hashlib.sha256()
        hasher2.update(self.ID)
        self.ID = hasher2.hexdigest()

        self.preferred = self.ID
        self.virtuous = True

    def IsPreferred(self):
        return self.preferred == self.ID

    def SetPreferred(self, txId):
        self.virtuous = txId == self.ID
        self.preferred = txId

    def Conflicts(self, tx):
        result = False
        for i1 in self.inputs:
            for i2 in tx.inputs:
                result = result or (i1.tx == i2.tx and i1.output == i2.output)
                if result:
                    break
            if result:
                break
        return result