from typing import List
from collections import defaultdict
import heapq


class Twitter:

  def __init__(self):
    self.time = 0
    self.tweetmap = defaultdict(list) # list of [time, tweetids] for userid
    self.followmap = defaultdict(set) # set of followeeids for userid

  def postTweet(self, userId: int, tweetId: int) -> None:
    self.tweetmap[userId].append([self.time, tweetId])
    self.time -= 1

  def getNewsFeed(self, userId: int) -> List[int]:
    result = []
    heap = []

    self.followmap[userId].add(userId)
    
    for followeeId in self.followmap[userId]:
      if followeeId in self.tweetmap:
        i = len(self.tweetmap[followeeId]) - 1
        time, tweetId = self.tweetmap[followeeId][i]
        heap.append([time, tweetId, followeeId, i - 1])

    heapq.heapify(heap)

    while heap and len(result) < 10:
      time, tweetId, followeeId, i = heapq.heappop(heap)
      result.append(tweetId)
      if i >= 0:
        time, tweetId = self.tweetmap[followeeId][i]
        heapq.heappush(heap, [time, tweetId, followeeId, i - 1])

    return result


  def follow(self, followerId: int, followeeId: int) -> None:
    self.followmap[followerId].add(followeeId)

  def unfollow(self, followerId: int, followeeId: int) -> None:
    if followeeId in self.followmap[followerId]:
      self.followmap[followerId].remove(followeeId)


def tests():
  twitter = Twitter()
  twitter.postTweet(1, 5)


def driver():
  tests()
