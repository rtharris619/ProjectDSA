# Write a function, linked_list_cycle, that takes in the head of a linked list as an argument. 
# The function should return a boolean indicating whether or not the linked list contains a cycle.

from structy.helpers.linked_list_helper import LinkedListNode as Node

def linked_list_cycle(head):
    if head is None or head.next is None:
        return False
    current = head
    value_set = set()
    while current is not None:
        if current.val in value_set:
            return True
        value_set.add(current.val)
        current = current.next
    return False

def linked_list_cycle_2(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

def driver():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    a.next = b
    b.next = c
    c.next = d
    d.next = b # cycle

    #         _______
    #       /        \
    # a -> b -> c -> d 

    res = linked_list_cycle_2(a)  # True
    print(res)

    q = Node('q')
    r = Node('r')
    s = Node('s')
    t = Node('t')
    u = Node('u')

    q.next = r
    r.next = s
    s.next = t
    t.next = u
    u.next = q # cycle

    #    ________________
    #  /                 \
    # q -> r -> s -> t -> u 

    res = linked_list_cycle_2(q)  # True
    print(res)

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d 
    res = linked_list_cycle_2(a)  # False
    print(res)