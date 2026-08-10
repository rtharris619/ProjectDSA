class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

class TreeHelper:
    def build_tree(self, nodes, f):
        val = next(nodes)
        num = int(next(nodes))
        children = [self.build_tree(nodes, f) for _ in range(num)]
        return Node(f(val), children)