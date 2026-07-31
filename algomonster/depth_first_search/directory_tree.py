import algomonster.helpers.binary_tree_helper as bt

indent_per_lvl = '  '
def print_tree(root: bt.Node, indent_lvl = '') -> None:
    if root is None:
        return
    print(indent_lvl + root.val)
    child_indent_lvl = indent_per_lvl + indent_lvl
    print_tree(root.left, child_indent_lvl)
    print_tree(root.right, child_indent_lvl)

def driver():
    encoded_tree = "/ foo baz x x x bar x x"
    helper = bt.BinaryTreeHelper()
    root = helper.build_tree(iter(encoded_tree.split(" ")), str)
    print_tree(root, '')