from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]):
  dummy = ListNode()
  tail = dummy

  while list1 and list2:
    if list1.val <= list2.val:
      tail.next = list1
      list1 = list1.next
    else:
      tail.next = list2
      list2 = list2.next

    tail = tail.next

  if list1:
    tail.next = list1
  elif list2:
    tail.next = list2

  return dummy.next
    


def tests():
  list1 = ListNode(1)
  list1.next = ListNode(2)
  list1.next.next = ListNode(4)

  list2 = ListNode(1)
  list2.next = ListNode(3)
  list2.next.next = ListNode(4)

  res = merge_two_lists(list1, list2)
  print(res.val)


def driver():
  tests()
