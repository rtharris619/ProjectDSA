from structy.helpers.linked_list_helper import LinkedListNode as Node

def is_univalue_list(head: Node):
    current = head
    while current is not None:
        if current.val != head.val:
            return False
        current = current.next
    return True

def is_univalue_list_rec(head: Node):

    def helper(current: Node):
        if current is None:
            return True
        if head.val != current.val:
            return False
        return helper(current.next)
    
    current = head
    return helper(current)

def is_univalue_list_rec2(head: Node, prev_val = None):
    if head is None:
        return True
    if prev_val is None or head.val == prev_val:
        return is_univalue_list_rec2(head.next, head.val)
    else:
        return False

def driver():
    u = Node(2)
    v = Node(2)
    w = Node(2)
    x = Node(2)
    y = Node(2)

    u.next = v
    v.next = w
    w.next = x
    x.next = y

    # 2 -> 2 -> 2 -> 2 -> 2

    res = is_univalue_list_rec(u) # True
    print(res)

    a = Node(7)
    b = Node(7)
    c = Node(4)

    a.next = b
    b.next = c

    # 7 -> 7 -> 4

    res = is_univalue_list_rec(a) # False
    print(res)
