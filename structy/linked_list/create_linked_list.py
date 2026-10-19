# Write a function, create_linked_list, that takes in a list of values as an argument. 
# The function should create a linked list containing each item of the list as the values of the nodes. 
# The function should return the head of the linked list.

from structy.helpers.linked_list_helper import LinkedList, LinkedListNode as Node

def create_linked_list(values):
    dummy = Node(None)
    tail = dummy
    for val in values:
        tail.next = Node(val)
        tail = tail.next
    return dummy.next

def driver():
    res = create_linked_list(["h", "e", "y"]) # h -> e -> y
    LinkedList().traverse(res)

    res = create_linked_list([1, 7, 1, 8]) # 1 -> 7 -> 1 -> 8
    LinkedList().traverse(res)

    res = create_linked_list(["a"]) # a
    LinkedList().traverse(res)

    res = create_linked_list([]) # null
    LinkedList().traverse(res)