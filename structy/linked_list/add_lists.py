# Write a function, add_lists, that takes in the head of two linked lists, each representing a number.
# The nodes of the linked lists contain digits as values.
# The nodes in the input lists are reversed; this means that the least significant digit of the number is the head.
# The function should return the head of a new linked list representing the sum of the input lists.
# The output list should have its digits reversed as well.

# You must do this by traversing through the linked lists once.

from structy.helpers.linked_list_helper import LinkedList, LinkedListNode as Node

def add_lists(head_1, head_2, carry = 0):
    if head_1 is None and head_2 is None and carry == 0:
        return None

    val_1 = 0 if head_1 is None else head_1.val
    val_2 = 0 if head_2 is None else head_2.val
    
    sum = val_1 + val_2 + carry
    carry = 1 if sum > 9 else 0
    digit = sum % 10
    res = Node(digit)

    next_1 = None if head_1 is None else head_1.next
    next_2 = None if head_2 is None else head_2.next

    res.next = add_lists(next_1, next_2, carry)
    return res

def add_lists_2(head_1, head_2):
    dummy = Node(None)
    tail = dummy
    current_1 = head_1
    current_2 = head_2
    carry = 0

    while current_1 is not None or current_2 is not None or carry == 1:
        val_1 = 0 if current_1 is None else current_1.val
        val_2 = 0 if current_2 is None else current_2.val
        sum = val_1 + val_2 + carry
        carry = 1 if sum > 9 else 0
        digit = sum % 10
        tail.next = Node(digit)
        tail = tail.next
        if current_1 is not None:
            current_1 = current_1.next
        if current_2 is not None:
            current_2 = current_2.next

    return dummy.next

def driver():
    #   621
    # + 354
    # -----
    #   975

    a1 = Node(1)
    a2 = Node(2)
    a3 = Node(6)
    a1.next = a2
    a2.next = a3
    # 1 -> 2 -> 6

    b1 = Node(4)
    b2 = Node(5)
    b3 = Node(3)
    b1.next = b2
    b2.next = b3
    # 4 -> 5 -> 3

    res = add_lists_2(a1, b1) # 5 -> 7 -> 9
    LinkedList().traverse(res)

    #  7541
    # +  32
    # -----
    #  7573

    a1 = Node(1)
    a2 = Node(4)
    a3 = Node(5)
    a4 = Node(7)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    # 1 -> 4 -> 5 -> 7

    b1 = Node(2)
    b2 = Node(3)
    b1.next = b2
    # 2 -> 3 

    res = add_lists_2(a1, b1) # 3 -> 7 -> 5 -> 7
    LinkedList().traverse(res)

    #   39
    # + 47
    # ----
    #   86

    a1 = Node(9)
    a2 = Node(3)
    a1.next = a2
    # 9 -> 3

    b1 = Node(7)
    b2 = Node(4)
    b1.next = b2
    # 7 -> 4

    res = add_lists_2(a1, b1) # 6 -> 8
    LinkedList().traverse(res)

    #   89
    # + 47
    # ----
    #  136

    a1 = Node(9)
    a2 = Node(8)
    a1.next = a2
    # 9 -> 8

    b1 = Node(7)
    b2 = Node(4)
    b1.next = b2
    # 7 -> 4

    res = add_lists(a1, b1) # 6 -> 3 -> 1
    LinkedList().traverse(res)
