class Solution:
    def isBipartite(self, graph: 'List[List[int]]') -> bool:
        # SOLUTION 1 - Using dfs
        def dfs(vertex):
            for neighbor in graph[vertex]:
                if neighbor in color:
                    if color[neighbor] == color[vertex]:
                        return False
                else:
                    color[neighbor] = 1 - color[vertex]
                    if not dfs(neighbor):
                        return False
            return True

        color = {}

        # Must check all node if graph is disjoint
        for vertex in range(len(graph)):
            if vertex not in color:
                color[vertex] = 0
                if not dfs(vertex):
                    return False
        return True
