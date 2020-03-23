import queue

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def isRoute(g: graph, a: Node, b: Node):
    if not a or not b:
        return False

    #create visited array 
    visted = {}
    for key in graph:
        visited[key] = False

    q = queue.Queue()
    q.put(a)
    while(not q.isEmpty()):
        node = q.pop()
        if node == b:
            return true 
        for neighbor in g[node]:
            

    
#tests 
graph = {
    1 : [2],
    2 : [3],
    3 : [4, 5],
    4 : [],
    5 : [], 
    6 : []
}

