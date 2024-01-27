
class Node:
    def __init__(self):
        self.value = -1
        self.left = None
        self.right = None


def insert_node(head, data):
    if head is None:
        head = Node()
        head.value = data
        return head

    if data > head.value:
        head.right = insert_node(head.right, data)
    else:
        head.left = insert_node(head.left, data)

    return head


def print_leaves(head):
    if head is None:
        return

    if head.left is None and head.right is None:
        print(str(head.value), end=", ")

    if head.left is not None:
        print_leaves(head.left)
    if head.right is not None:
        print_leaves(head.right)


def test():
    root = Node()
    lst = [100, 80, 50, 90, 30, 60, 90, 85, 95, 120, 110, 108, 115, 140, 150]

    for item in lst:
        insert_node(root, item)

    print_leaves(root)
