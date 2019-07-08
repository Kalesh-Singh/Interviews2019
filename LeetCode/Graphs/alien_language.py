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
from collections import defaultdict


# TODO: Not correct

def addEdgesHelper(words, graph):
    curr = 0
    while curr < len(words) - 1:
        if words[curr][0] != words[curr + 1][0]:
            graph.addEdge(ord(words[curr][0]) - ord('a'), ord(words[curr + 1][0]) - ord('a'))


def addEdges(words, graph):
    addEdgesHelper(words, graph)
    groups = getGroups(words)
    for group in groups:
        addEdges(group, graph)


def getGroups(words):
    groups = defaultdict(list)
    for word in group:
        if len(word[1:]) > 0:
            newGroups[word[0]].append(word[1:])
    return groups.values()


def printOrder(words, alpha):
    graph = Graph(alpha)
    addEdges(words, graph)
    return graph.topologicalSort()
