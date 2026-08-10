import algomonster.helpers.tree_helper as tt

def ternary_tree_paths(root: tt.Node) -> list[str]:
    def dfs(root: tt.Node, path: list[str], res: list[str]) -> list[str]:
        if len(root.children) == 0:
            res.append("->".join(path + [str(root.val)]))
            return

        for child in root.children:
            path.append(str(root.val))
            dfs(child, path, res)
            path.pop()

    res: list[str] = []
    dfs(root, [], res)
    return res

def driver():
    helper = tt.TreeHelper()
    encoded_tree = "1 3 2 1 5 0 3 0 4 0"
    tree = helper.build_tree(iter(encoded_tree.split(" ")), int)
    res = ternary_tree_paths(tree)
    for line in res:
        print(line)