from structy.helpers.linked_list_helper import LinkedListNode as Node

def sum_list(head: Node):
    total = 0
    current = head
    while current is not None:
        total += current.val
        current = current.next
    return total

def sum_list_rec(head: Node):
    if head is None:
        return 0
    return head.val + sum_list_rec(head.next)

def driver():
    a = Node(2)
    b = Node(8)
    c = Node(3)
    d = Node(-1)
    e = Node(7)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    res = sum_list_rec(a)
    print(res)