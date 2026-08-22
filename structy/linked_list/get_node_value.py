from structy.helpers.linked_list_helper import LinkedListNode as Node

def get_node_value(head: Node, index: int) -> str:
    current = head
    count = 0
    while current is not None:
        if count == index:
            return current.val
        current = current.next
        count += 1
    return None

def get_node_value_rec(head: Node, index: int) -> str:
    if head is None:
        return None
    if index == 0:
        return head.val
    return get_node_value_rec(head.next, index - 1)

def driver():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    res = get_node_value_rec(a, 2) # 'c'
    print(res)