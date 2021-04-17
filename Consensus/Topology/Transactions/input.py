class Input:
    def __init__(self, txId, output, script):
        # Origin transaction's ID (string)
        self.tx = txId
        # Which output from the transaction we're using (hex)
        self.output = output