INT_MAX = 4294967296
INT_MIN = -4294967296


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBSTUtil(node, mini, maxi):
    if node is None:
        return True
    if node.data < mini or node.data > maxi:
        return False
    return (checkBSTUtil(node.left, mini, node.data - 1) and checkBSTUtil(node.right, node.data+1, maxi))


def checkBST(root):
    return (checkBSTUtil(root, INT_MIN, INT_MAX))
