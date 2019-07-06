# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # SOLUTION 1 - Using DFS and a map between
        # original and cloned nodes
        if not node:
            return None

        clone, stack = {}, [node]
        clone[node] = Node(node.val, [])

        while stack:
            vertex = stack.pop()
            for neighbor in vertex.neighbors:
                if neighbor not in clone:
                    stack.append(neighbor)
                    clone[neighbor] = Node(neighbor.val, [])
                clone[vertex].neighbors.append(clone[neighbor])

        return clone[node]
