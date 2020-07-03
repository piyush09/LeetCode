import collections
class Node:
    def __init__(self, val=0, neighbors = None):

        self.val = val
        if neighbors is not None:
            self.neighbors = neighbors
        else:
            self.neighbors = []

def cloneGraph1(node):
    if not node:
        return
    nodeCopy = Node(node.val, [])
    dic = {node: nodeCopy}
    queue = collections.deque([node])
    while queue:
        node = queue.popleft()
        for neighbor in node.neighbors:
            if neighbor not in dic: # neighbor is not visited
                neighborCopy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                queue.append(neighbor)
            else:
                dic[node].neighbors.append(dic[neighbor])
    return nodeCopy

adjList = [[2,4],[1,3],[2,4],[1,3]]
print (cloneGraph1(node))