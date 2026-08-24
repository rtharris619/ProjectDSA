from structy.helpers.linked_list_helper import LinkedListNode as Node

def reverse_list(head: Node):
    prev = None
    current = head
    next = head.next

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

def reverse_list_rec(head: Node, prev = None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverse_list_rec(next, head)

def traverse(head: Node):
    current = head
    while current is not None:
        print(current.val)
        current = current.next

def driver():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # a -> b -> c -> d -> e -> f
    res = reverse_list_rec(a) # f -> e -> d -> c -> b -> a
    traverse(res)