from structy.helpers.linked_list_helper import LinkedList, LinkedListNode as Node

def insert_node(head: Node, value, index: int) -> Node:
    if index == 0:
        new_node = Node(value)
        new_node.next = head
        return new_node
    count = 0
    current = head
    while current is not None:
        if count == index - 1:
            next = current.next
            current.next = Node(value)
            current.next.next = next
        current = current.next
        count += 1
    return head

def insert_node_rec(head: Node, value, index: int, count = 0) -> Node:
    if index == 0:
        new_head = Node(value)
        new_head.next = head
        return new_head
    if count == index - 1:
        next = head.next
        head.next = Node(value)
        head.next.next = next
        return
    insert_node_rec(head.next, value, index, count + 1)
    return head

def driver():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    res = insert_node_rec(a, 'v', 3)
    # a -> b -> c -> v -> d
    LinkedList().traverse(res)