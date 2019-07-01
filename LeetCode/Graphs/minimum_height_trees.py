# TODO: Read geeks for geeks
# https://www.geeksforgeeks.org/roots-tree-gives-minimum-height/


from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: 'List[List[int]]') -> 'List[int]':
        degree = [0] * n
        leaves = []

        if n == 1:
            leaves.append(0)
            return leaves

        graph_map = defaultdict(set)

        for i in range(len(edges)):
            a = edges[i][0]
            b = edges[i][1]

            graph_map[a].add(b)
            graph_map[b].add(a)

            degree[a] += 1
            degree[b] += 1

        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)

        new_leaves = []

        while n > 2:
            n -= len(leaves)

            for i in range(len(leaves)):
                curr = leaves.pop()
                neighbors = graph_map[curr]

                for neighbor in neighbors:
                    degree[neighbor] -= 1
                    graph_map[neighbor].remove(curr)

                    if degree[neighbor] == 1:
                        new_leaves.append(neighbor)

            leaves = new_leaves
            new_leaves = []

        return leaves


