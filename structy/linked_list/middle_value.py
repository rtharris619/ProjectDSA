# Write a function, middle_value, that takes in the head of a linked list as an argument. 
# The function should return the value of the middle node in the linked list. 
# If the linked list has an even number of nodes, then return the value of the second middle node.
# You may assume that the input list is non-empty.

from structy.helpers.linked_list_helper import LinkedListNode as Node

def middle_value(head):
    if head.next is None:
        return head.val
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

def driver():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    # a -> b -> c -> d -> e
    res = middle_value(a) # c
    print(res)

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # a -> b -> c -> d -> e -> f
    res = middle_value(a) # d
    print(res)
