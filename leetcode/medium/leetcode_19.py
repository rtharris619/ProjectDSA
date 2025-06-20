from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int):
  dummy = ListNode(0, head)
  left = dummy
  right = head

  while n > 0 and right:
    right = right.next
    n -= 1

  while right:
    right = right.next
    left = left.next

  left.next = left.next.next

  return dummy.next 


def tests():
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)

  remove_nth_from_end(head, 2)


def driver():
  tests()
