# Implement the enqueue and dequeue methods for the existing class.
# The enqueue method should add a given value into the queue. 
# The dequeue should return and remove an item from the queue following first-in, first-out order.
# Your implementation should use a linked-list and not any built in containers.

from structy.helpers.linked_list_helper import LinkedListNode as Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def enqueue(self, val):
        if self.size == 0:
            self.head = self.tail = Node(val)
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next # sets the stage for enqueueing a new node
        self.size += 1
 
    def dequeue(self):
        if self.size == 0:
            return 0
        val = self.head.val
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next # to remove node
        self.size -= 1
        return val

def driver():
    queue = Queue()
    queue.enqueue("a")
    queue.size # -> 1
    res = queue.dequeue() # -> a
    print(res)
    queue.enqueue("b")
    queue.enqueue("c")
    queue.size # -> 2
    res = queue.dequeue() # -> b
    print(res)
    res = queue.dequeue() # -> c
    print(res)
    res = queue.size # -> 0
    print(res)