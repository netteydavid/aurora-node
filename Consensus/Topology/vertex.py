import math
from .decidable import Decidable
from ..factories import GetHash256, GetMerkleTree
from ..constants import Status

class Vertex(Decidable):
    def __init__(self, version, parents, chit, txs):
        self.version = version
        self.parents = parents
        self.transactions = {}
        for tx in txs:
            self.transactions[tx.Id] = tx
        # Generate Merkle root
        self.txroot = GetMerkleTree(self.transactions)[0]
        #TODO: Generate ID
        self.chit = chit
        self.confidence = 0
        self.successes = 0
        #TODO: Is there a count of failures?
        if chit:
            self.confidence = 1
            self.successes = 1
        super().__init__()

    def IsPreferred(self):
        result = True
        for tx in self.transactions.values():
            result = result and tx.IsPreferred()
        return result

    def IsVirtuous(self):
        result = True
        for tx in self.transactions.values():
            result = result and tx.virtuous
        return result
