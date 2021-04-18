#TODO: Fill this out when the time is right
"""
This is a unit of a secondary DAG structure. Each vertex is a transaction output. 
This will have the transaction id, output number, parents (the vertices that were spent to create it), 
and whether the output has be settled or not. A service will refer to the DAG to see if a transaction has been settled. 
The service can also use the DAG to see if a transaciton is virtuous or has a conflict set.
When an output has been settled, a recursive method will update all unsettled parents. Only the unsettled portion of the DAG 
is held in memory.
"""
class Output_Vertex:
    pass