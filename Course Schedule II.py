import collections
# DFS Implementation in iterative way using stack

def findOrder(numCourses, prerequisites):
    # 'indegreeDictionary' is the set of all nodes that point to the current node (indegree)
    indegreeDictionary = collections.defaultdict(set)

    # 'outDegreeDictionary' stores the input node (course) and set of all the next possible nodes (courses) from it (outdegree)
    outDegreeDictionary = collections.defaultdict(set)
    for i, j in prerequisites:
        indegreeDictionary[i].add(j)
        outDegreeDictionary[j].add(i)

    # 'stack' is the list of all the nodes, that don't have edges pointing to them (indegree = 0)
    stack = []
    for i in range(numCourses):
        if not indegreeDictionary[i]:
            stack.append(i)

    res = []

    # DFS Algorithm applied for all nodes in the 'stack'
    while stack:
        # Getting the node value, appending it to result
        # Getting it in order to iterate over all the outdegree neighbors of the node
        node = stack.pop()
        res.append(node)
        for i in outDegreeDictionary[node]:
            indegreeDictionary[i].remove(node) # Remove the current iterating node that points to inDegreeDictionary[i] node
            if not indegreeDictionary[i]:
                stack.append(i)
        # Popping the node which was initially popped from the stack, from the indegree dictionary (inDegreeDictionary)
        indegreeDictionary.pop(node)

    # If inDegreeDictionary is empty, then return 'res' as the required result
    if not indegreeDictionary:
        return res
    else:
        return []

# numCourses = 4
# prerequisites = [[1,0],[2,0],[3,1],[3,2]]

# numCourses = 2
# prerequisites = []

numCourses = 3
prerequisites = [[1,0]]

print (findOrder(numCourses, prerequisites))