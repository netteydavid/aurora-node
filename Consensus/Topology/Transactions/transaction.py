import hashlib
from ..decidable import Decidable
from ...factories import GetRawTx, GetHash256

class Transaction:
    def __init__(self, txid, wid, version, inputs, outputs, witness):
        
        #Get raw tx data
        txRaw = GetRawTx(version, inputs, outputs)
        # First hashing
        genId = GetHash256(txRaw)
        # Second hashing
        genId = GetHash256(genId)
        # Check if tx ids match
        if txid != genId:
            raise Exception("Invalid transaction id")
        
        witId = GetHash256(witness)
        witId = GetHash256(witId)
        #Check if the witness Ids match
        if wid != witId:
            raise Exception("Invalid transaction id")
            
        # Tx and witness Ids
        self.Id = txid
        self.witnessId = wid
        # Version number (hex)
        self.version = version
        # Inputs, outputs this transaction spends
        self.inputs = inputs
        # Outputs this transaction generates
        self.outputs = outputs
        # Witness data
        self.witness = witness
        # Assume virtuosity until otherwise stated
        self.preferred = self.Id
        self.virtuous = True

    def IsPreferred(self):
        return self.preferred == self.Id

    def SetPreferred(self, txId):
        self.virtuous = txId == self.Id
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