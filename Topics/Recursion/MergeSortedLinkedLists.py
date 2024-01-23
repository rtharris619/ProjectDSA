
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def sorted_merge(a: Node, b: Node):
    if a is None:
        return b
    if b is None:
        return a

    if a.value <= b.value:
        a.next = sorted_merge(a.next, b)
        return a
    else:
        b.next = sorted_merge(a, b.next)
        return b


def test():
    a = Node(1)
    a.next = Node(5)
    a.next.next = Node(13)
    a.next.next.next = Node(14)
    a.next.next.next.next = Node(550)

    b = Node(2)
    b.next = Node(15)
    b.next.next = Node(130)
    b.next.next.next = Node(200)
    b.next.next.next.next = Node(550)

    c = sorted_merge(a, b)

    while c:
        print(c.value)
        c = c.next
