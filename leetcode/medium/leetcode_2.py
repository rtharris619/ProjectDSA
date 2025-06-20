from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def traverse_linked_list(head: Optional[ListNode]):
  curr = head
  while curr:
    print(curr.val)
    curr = curr.next
  print()


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
  
  dummy = ListNode()
  tail = dummy

  carry = False
  while l1 or l2 or carry:

    v1plusv2 = (l1.val if l1 else 0) + (l2.val if l2 else 0)
    val = v1plusv2 + 1 if carry else v1plusv2

    if val < 10:
      tail.next = ListNode(val)
      carry = False
    else:
      tail.next = ListNode(val - 10)
      carry = True

    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None
    tail = tail.next

  return dummy.next


def test1():
  l1 = ListNode(2)
  l1.next = ListNode(4)
  l1.next.next = ListNode(3)

  l2 = ListNode(5)
  l2.next = ListNode(6)
  l2.next.next = ListNode(4)

  res = add_two_numbers(l1, l2)
  traverse_linked_list(res)


def test2():
  l1 = ListNode(9)
  l1.next = ListNode(9)

  l2 = ListNode(9)
  l2.next = ListNode(9)
  res = add_two_numbers(l1, l2)
  traverse_linked_list(res)


def test3():
  l1 = ListNode(7)
  l2 = ListNode(8)
  res = add_two_numbers(l1, l2)
  traverse_linked_list(res)


def test4():
  l1 = ListNode(5)
  l1.next = ListNode(6)
  l1.next.next = ListNode(4)

  l2 = ListNode(2)
  l2.next = ListNode(4)
  l2.next.next = ListNode(3)
  l2.next.next.next = ListNode(3)

  res = add_two_numbers(l1, l2)
  traverse_linked_list(res)


def tests():
  test4()


def driver():
  tests()
