import algomonster.helpers.binary_tree_helper as bt

def tree_max_depth(root: bt.Node) -> int:
    def dfs(root: bt.Node, lvl: int) -> int:
        if root is None:
            return lvl
        lvl += 1
        return max(dfs(root.left, lvl), dfs(root.right, lvl))
    return 0 if root is None else dfs(root, -1)

def tree_max_depth_2(root: bt.Node) -> int:
    def dfs(root: bt.Node):
        if root is None:
            return 0
        return max(dfs(root.left), dfs(root.right)) + 1
    return 0 if root is None else dfs(root) - 1

def driver():
    encoded_tree = "5 4 3 x x 8 x x 6 x x"
    helper = bt.BinaryTreeHelper()
    root = helper.build_tree(iter(encoded_tree.split(" ")), int)
    res = tree_max_depth_2(root)
    print(res)