from typing import Optional


class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


def has_cycle(head: Optional[ListNode]) -> bool:
  
  hashmap = {}
  curr = head
  while curr:
    if curr in hashmap:
      return True
    hashmap[curr] = True
    curr = curr.next
      
  return False


def has_cycle_2(head: Optional[ListNode]) -> bool:
  slow, fast = head, head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
      return True

  return False


def test1():
  head = ListNode(3)
  head.next = ListNode(2)
  head.next.next = ListNode(0)
  head.next.next.next = ListNode(-4)
  head.next.next.next.next = head.next
  res = has_cycle_2(head)
  print(res)


def test2():
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = head
  res = has_cycle_2(head)
  print(res)


def test3():
  head = ListNode(1)
  res = has_cycle_2(head)
  print(res)


def tests():
  test1()
  test2()
  test3()


def driver():
  tests()
