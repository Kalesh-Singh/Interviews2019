from collections import defaultdict


def has_cycle(graph, start_node, visiting: set, visited: set):
    if start_node in visited:
        return False
    if start_node in visiting:
        return True

    visiting.add(start_node)

    if start_node in graph:
        for neighbor in graph[start_node]:
            if has_cycle(graph, neighbor, visiting, visited):
                return True

    visiting.remove(start_node)
    visited.add(start_node)

    return False


class Solution:
    def canFinish(self, numCourses: int, prerequisites: 'List[List[int]]') -> bool:
        # Build adjacency lists
        graph = defaultdict(set)
        for start, end in prerequisites:
            graph[start].add(end)

        # Detect cycle using dfs
        visited, visiting = set(), set()
        for node in graph:
            if has_cycle(graph, node, visiting, visited):
                return False
        return True
