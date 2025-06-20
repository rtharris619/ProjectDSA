from typing import Optional


class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random


def check_linked_list(head: 'Optional[Node]'):
  curr = head
  while curr:
    print(curr.val, " -> ", curr.random.val if curr.random else 'None')
    curr = curr.next
  print()


def check_dictionary(dictionary: dict):
  for i, v in enumerate(dictionary):
    print(v.val if v else 'None', " -> ", v.random.val if v and v.random else 'None')


def copy_random_list(head: 'Optional[Node]') -> 'Optional[Node]':
  
  copy = { None : None }

  curr = head
  while curr:
    copy[curr] = Node(curr.val)
    curr = curr.next

  curr = head
  while curr:
    cp = copy[curr]
    cp.next = copy[curr.next]
    cp.random = copy[curr.random]
    curr = curr.next

  check_dictionary(copy)

  return copy[head]


def tests():
  head = Node(7)
  head.next = Node(13)
  head.next.next = Node(11)
  head.next.next.next = Node(10)
  head.next.next.next.next = Node(1)
  head.next.next.next.next.next = None

  head.random = None
  head.next.random = head
  head.next.next.random = head.next.next.next.next
  head.next.next.next.random = head.next.next
  head.next.next.next.next.random = head

  copy_random_list(head)


def driver():
  tests()
