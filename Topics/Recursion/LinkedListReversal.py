
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_linked_list(head):
    current = head
    while current:
        print(current.value)
        current = current.next


def reverse_linked_list(head):
    if head is None or head.next is None:
        return head

    new_head = reverse_linked_list(head.next)

    head.next.next = head
    head.next = None

    return new_head


def test():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original Linked List")
    print_linked_list(head)

    print("Reversed Linked List")
    new_head = reverse_linked_list(head)
    print_linked_list(new_head)
