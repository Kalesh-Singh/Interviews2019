"""
This function finds and returns the order
of characers from a sorted array of words.
alpha is number of possible alphabets
starting from 'a'. For simplicity, this
function is written in a way that only
first 'alpha' characters can be
in words array. For example if alpha
is 7, then words[] should contain words
having only 'a', 'b','c' 'd', 'e', 'f', 'g'

Graph class
 Graph(numVertices)
 addEdge(startVertex, endVertex)
 topologicalSort()
    rtype: List[char]
"""
from collections import defaultdict, deque


class Graph(object):
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(set)

    def add_edge(self, start_vertex, end_vertex):
        self.graph[start_vertex].add(end_vertex)

    def _dfs(self, start_node, visited, sorted_list):
        visited.add(start_node)
        if start_node in self.graph:
            for neighbor in self.graph[start_node]:
                if neighbor not in visited:
                    self._dfs(neighbor, visited, sorted_list)
        sorted_list.appendleft(start_node)

    def topological_sort(self):
        visited, sorted_list = set(), deque()
        for node in self.graph:
            if node not in visited:
                self._dfs(node, visited, sorted_list)
        return list(sorted_list)


def print_order(words, alpha):
    # Build the graph
    graph = Graph(alpha)
    for i in range(len(words) - 1):
        # For every pair of adjacent words
        word1, word2 = words[i], words[i + 1]
        for start, end in zip(word1, word2):
            # Add edge for first pair of mismatched characters
            if start != end:
                graph.add_edge(start, end)
                break

    print(graph.graph)
    # Do a topological sort
    return graph.topological_sort()


def test_print_order():
    assert print_order(['caa', 'aaa', 'aab'], 3) == ['c', 'a', 'b']
    assert print_order(['baa', 'abcd', 'abca', 'cab', 'cad'], 4) == ['b', 'd', 'a', 'c']
