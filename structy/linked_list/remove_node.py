from structy.helpers.linked_list_helper import LinkedList, LinkedListNode as Node

def remove_node(head: Node, target_val) -> Node:
    if head.val == target_val:
        return head.next

    prev = None
    current = head

    while current is not None:
        if current.val == target_val:
            prev.next = current.next
            break
        prev = current
        current = current.next
    return head

def remove_node_rec(head: Node, target_val) -> Node:
    if head is None:
        return None
    if head.val == target_val:
       return head.next
    head.next = remove_node_rec(head.next, target_val)
    return head

def driver():
    node1 = Node("h")
    node2 = Node("i")
    node3 = Node("j")
    node4 = Node("i")

    node1.next = node2
    node2.next = node3
    node3.next = node4

    # h -> i -> j -> i

    res = remove_node_rec(node1, "i")
    # h -> j -> i

    LinkedList().traverse(res)