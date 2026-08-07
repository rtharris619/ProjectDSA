import algomonster.helpers.binary_tree_helper as bt
from math import inf

def valid_bst(root: bt.Node) -> bool:
    ls = []
    def dfs(root: bt.Node):
        if root is None:
            return True
        dfs(root.left)
        if len(ls) > 0 and ls[-1] > root.val:
            return False
        ls.append(root.val)
        dfs(root.right)
        return True
    return dfs(root)

def valid_bst_2(root: bt.Node) -> bool:
    def dfs(root: bt.Node, min_val: int, max_val: int):
        if root is None:
            return True
        if min_val > root.val or max_val < root.val:
            return False
        return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)
    return dfs(root, -inf, inf)

def driver():
    helper = bt.BinaryTreeHelper()
    encoded_tree = "6 4 3 x x 8 x x 8 x x"
    root = helper.build_tree(iter(encoded_tree.split(" ")), int)
    res = valid_bst_2(root)
    print(res)