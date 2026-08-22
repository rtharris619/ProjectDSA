from structy.helpers.linked_list_helper import LinkedListNode as Node

def linked_list_values(head: Node) -> list[int]:
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values

def linked_list_values_rec(head: Node) -> list[int]:
    values = []
    fill_values(head, values)
    return values

def fill_values(head: Node, values: list[int]):
    if head is None:
        return
    values.append(head.val)
    fill_values(head.next, values)

def driver():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    res = linked_list_values_rec(a)
    print(res)