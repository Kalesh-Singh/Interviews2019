# TODO: Needs fixing

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None


def level_order(node, serial):
    if node:
        serial.append(str(node.val))
        level_order(node.left, serial)
        level_order(node.right, serial)
    else:
        serial.append('null')


def helper(data, i=0):
    if data[i] == 'null':
        return None
    root = TreeNode(int(data[i]))
    root.left = helper(data, i + 1)
    root.right = helper(data, i + 1)
    return root


def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    serial = []
    level_order(root, serial)
    return ','.join(serial)


def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    serialized_tree = data.split(',')
    return helper(serialized_tree)
