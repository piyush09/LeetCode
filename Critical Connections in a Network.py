import collections

class Solution:
    def criticalConnections(self, n, connections):

        def makeGraph(connections):

            # default items are created using list() which returns new empty list object
            graph = collections.defaultdict(list)

            for item in connections:
                graph[item[0]].append(item[1])
                graph[item[1]].append(item[0])

            return graph

        # Making a graph for the given connections
        graph = makeGraph(connections)

        connections = set(map(tuple, map(sorted, connections)))

        # Assigning rank of (-2) to each node
        rank = [-2] * n

        def dfs(node, depth):

            if rank[node] >= 0:  # visiting (0<=rank<n), or visited(rank=n)
                return rank[node]

            rank[node] = depth
            min_back_depth = n

            for neighbour in graph[node]:
                if (rank[neighbour] == depth - 1):
                    continue

                back_depth = dfs(neighbour, depth + 1)
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbour))))
                min_back_depth = min(min_back_depth, back_depth)

            rank[node] = n
            return min_back_depth

        # As it is a connected graph, no need to loop over all the nodes
        dfs(0, 0)

        return list(connections)

n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]

print (Solution().criticalConnections(n, connections))