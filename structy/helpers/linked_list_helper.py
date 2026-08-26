class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def traverse(self, head: LinkedListNode):
        if head is None:
            print()
            return
        print(head.val, end=" ")
        self.traverse(head.next)