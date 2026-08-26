from structy.helpers.linked_list_helper import LinkedListNode as Node

def longest_streak(head: Node):
    max_streak = 0
    current_streak = 0
    prev_val = None
    current = head

    while current is not None:
        if prev_val == current.val:
            current_streak += 1
        else:
            current_streak = 1
        if current_streak > max_streak:
            max_streak = current_streak
        prev_val = current.val
        current = current.next

    return max_streak

def longest_streak_rec(head: Node, current_streak = 0, max_streak = 0, prev_val = None):
    if head is None:
        return max_streak
    if prev_val == head.val:
        current_streak += 1
    else:
        current_streak = 1
    if current_streak > max_streak:
        max_streak = current_streak
    return longest_streak_rec(head.next, current_streak, max_streak, head.val)

def driver():
    a = Node(9)
    b = Node(9)
    c = Node(1)
    d = Node(9)
    e = Node(9)
    f = Node(9)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # 9 -> 9 -> 1 -> 9 -> 9 -> 9

    res = longest_streak_rec(a) # 3
    print(res)