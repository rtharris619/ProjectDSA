from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:

  prev, curr = None, head

  while curr:
    tmp = curr.next
    curr.next = prev
    prev = curr
    curr = tmp

  return prev


def reverse_list_recursive(head: ListNode) -> ListNode:
  def reverse(curr, prev):
    if curr is None:
      return prev
    else:
      temp = curr.next
      curr.next = prev
      return reverse(temp, curr)

  return reverse(head, None)


def tests():
  linkedlist = ListNode(1)
  linkedlist.next = ListNode(2)
  linkedlist.next.next = ListNode(3)
  linkedlist.next.next.next = ListNode(4)
  linkedlist.next.next.next.next = ListNode(5)

  print(reverse_list_recursive(linkedlist).val)


def driver():
  tests()
