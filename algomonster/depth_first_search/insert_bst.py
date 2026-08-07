import algomonster.helpers.binary_tree_helper as bt

def insert_bst(bst: bt.Node, val: int) -> bt.Node:
    if bst is None:
        return bt.Node(val)
    if bst.val > val:
        bst.left = insert_bst(bst.left, val)
    elif bst.val < val:
        bst.right = insert_bst(bst.right, val)
    return bst
    
def preorder_traversal(bst: bt.Node):
    if bst is not None:
        print(bst.val)
        preorder_traversal(bst.left)        
        preorder_traversal(bst.right)

def driver():
    helper = bt.BinaryTreeHelper()
    encoded_tree = "8 5 2 x 3 x x 6 x x 10 x 14 x x"
    bst = helper.build_tree(iter(encoded_tree.split(" ")), int)
    bst = insert_bst(bst, 7)
    preorder_traversal(bst)