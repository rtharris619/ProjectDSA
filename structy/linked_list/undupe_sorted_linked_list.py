# Write a function that takes in a linked list that contains values in increasing order. 
# The function should return a new linked list containing the original values, with duplicates removed. 
# The relative order of values in the resulting linked list should be unchanged.
# You must create and return a new set of linked list nodes and not just modify the input nodes.

from structy.helpers.linked_list_helper import LinkedList, LinkedListNode as Node

def undupe_sorted_linked_list(head):
    dummy = Node(None)
    tail = dummy
    current = head
    while current is not None:
        if current.val != tail.val:
            tail.next = Node(current.val)
            tail = tail.next
        current = current.next

    return dummy.next

def driver():
    a = Node(4)
    b = Node(4)
    c = Node(6)
    d = Node(6)
    e = Node(6)
    f = Node(7)
    g = Node(7)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g

    # 4 -> 4 -> 6 -> 6 -> 6 -> 7 -> 7
    res = undupe_sorted_linked_list(a) # 4 -> 6 -> 7
    LinkedList().traverse(res)

    w = Node(5)
    x = Node(5)
    y = Node(5)
    z = Node(8)

    w.next = x
    x.next = y
    y.next = z

    # 5 -> 5 -> 5 -> 8
    res = undupe_sorted_linked_list(x) # 5 -> 8
    LinkedList().traverse(res)
    