from ..constants import Status

class Vertex_Graph:
    def __init__(self, vertices):
        self.vertices = {}
        for vertex in vertices:
            self.vertices[vertex.Id] = vertex

    def IsStronglyPreferred(self, vid):
        vertex = self.vertices[vid]
        #status is none, determine if strongly preferred
        retVal = vertex.IsPreferred()
        for parent in vertex.parents:
            #Check if ancestors are strongly preferred as well
            retVal = retVal and self.IsStronglyPreferred(parent)
        return retVal

    def IsAccepted(self, vid, beta1, beta2):
        vertex = self.vertices[vid]
        # Check if status has already been changed
        if vertex.status == Status.accepted:
            return True
        elif vertex.status == Status.rejected:
            return False
        
        # Safe early commitment
        result = vertex.IsVirtuous()
        for parent in vertex.parents:
            result = result and self.IsAccepted(parent, beta1, beta2)
        result = result and vertex.confidence >= beta1

        # Check consecutive counter
        result = result or vertex.successes >= beta2

        # If it is accepted, change status to accepted
        if result:
            vertex.Accept()

        return result

    def Update(self, vid, chit, beta1, beta2):
        vertex = self.vertices[vid]
        if chit:
            vertex.confidence += 1
            vertex.successes += 1
        else:
            vertex.successes = 0
        for parent in vertex.parents:
            self.Update(parent, chit, beta1, beta2)
        self.IsAccepted(vid, beta1, beta2)
        #TODO: If accepted, serialize and save vertex. remove from dict
    
    def Add(self, vertex, beta1, beta2):
        self.vertices[vertex.Id] = vertex
        for parent in vertex.parents:
            self.Update(parent, vertex.chit, beta1, beta2)