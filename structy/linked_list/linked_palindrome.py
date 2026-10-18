# Write a function, linked_palindrome, that takes in the head of a linked list as an argument. 
# The function should return a boolean indicating whether or not the linked list is a palindrome. 
# A palindrome is a sequence that is the same both forwards and backwards.

from structy.helpers.linked_list_helper import LinkedListNode as Node


def linked_palindrome(head):
    if not head:
        return True
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values == values[::-1]


def linked_palindrome_2(head):
    if head is None:
        return True
    values = []
    linked_palindrome_helper(head, values)
    return values == values[::-1]


def linked_palindrome_helper(current, values):
    if current is None:
        return True
    values.append(current.val)
    linked_palindrome_helper(current.next, values)


def is_palindrome(values: list[int]):
    left = 0
    right = len(values) - 1
    while left <= right:
        if values[left] != values[right]:
            return False
        left += 1
        right -= 1
    return True


def driver():
    a = Node(3)
    b = Node(2)
    c = Node(7)
    d = Node(7)
    e = Node(2)
    f = Node(3)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # 3 -> 2 -> 7 -> 7 -> 2 -> 3
    res = linked_palindrome_2(a) # True
    print(res)

    a = Node(3)
    b = Node(2)
    c = Node(4)

    a.next = b
    b.next = c

    # 3 -> 2 -> 4
    res = linked_palindrome_2(a) # False
    print(res)
