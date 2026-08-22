from structy.helpers.linked_list_helper import LinkedListNode as Node

def linked_list_find(head: Node, target) -> bool:
    current = head
    while current is not None:
        if current.val == target:
            return True
        current = current.next
    return False

def linked_list_find_rec(head: Node, target) -> bool:
    if head is None:
        return False
    if head.val == target:
        return True
    return linked_list_find_rec(head.next, target)

def driver():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    res = linked_list_find_rec(a, "c") # True
    print(res)