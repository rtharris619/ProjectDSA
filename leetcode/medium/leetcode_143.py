from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def reorder_list(head: Optional[ListNode]):
  lst = []

  curr = head

  while curr:
    lst.append(curr)
    curr = curr.next
  
  L = 0
  R = len(lst) - 1

  while L < R:
    lst[L].next = lst[R]
    L += 1
    lst[R].next = lst[L]
    R -= 1

  lst[L].next = None

  # Checking...
  curr = head
  while curr:
    print(curr.val, end=" ")
    curr = curr.next
  print()



def tests():

  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)

  reorder_list(head)


def driver():
  tests()
