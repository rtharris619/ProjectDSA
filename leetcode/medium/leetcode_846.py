from typing import List
import heapq

class Solution:
  def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize:
      return False
    
    cardCount = {}
    for card in hand:
      cardCount[card] = 1 + cardCount.get(card, 0)
    minHeap = list(cardCount.keys())
    heapq.heapify(minHeap)

    while minHeap:
      first = minHeap[0]
      for card in range(first, first + groupSize):
        if card not in cardCount:
          return False
        cardCount[card] -= 1
        if cardCount[card] == 0:
          if card != minHeap[0]:
            return False
          heapq.heappop(minHeap)
        
    return True
  

def tests():
  hand, groupSize = [1,2,3,6,2,3,4,7,8], 3
  print(Solution().isNStraightHand(hand, groupSize))

def driver():
  tests()
