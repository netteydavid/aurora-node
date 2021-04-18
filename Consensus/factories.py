import hashlib, math

# Returns the sha256 in hex of the input
def GetHash256(input):
    hasher = hashlib.sha256()
    hasher.update(input)
    return hasher.hexdigest()

def GetRawTx(version, inputs, outputs):
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
    return hex(int(tx, 16))

def GetMerkleTree(ids):
    if (ids < 1):
        return
    if (ids == 1):
        return ids
    level = ids
    temp = []
    rTree = []
    while (len(level) > 1):
        for i in range(len(level)):
            element = str(level[i])
            j = i + 1
            if j < len(level):
                element1 = str(level[j])
                concat = element + element1
                result = GetHash256(hex(int(concat, 16)))
                temp.append(result)
                rTree.append(result)
            else:
                temp.append(level[i])
                rTree.append(level[i])
        level = temp
        temp = []
    
    rTree.reverse()
    tree = []
    n = 0
    for i in range(0, len(rTree), 2**n):
        if i + 2**n < len(rTree):
            for item in rTree[i:2**n].reverse():
                tree.append(item)
        else:
            for item in rTree[i:].reverse():
                tree.append(item)
        n += 1

    return tree