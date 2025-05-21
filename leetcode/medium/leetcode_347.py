
def top_k_frequent(nums: list[int], k: int) -> list[int]:
  count = {}
  freq = [[] for i in range(len(nums) + 1)]

  for n in nums:
    count[n] = 1 + count.get(n, 0)

  for n, c in count.items():
    freq[c].append(n)

  res = []
  for i in range(len(freq) - 1, 0, -1):
    for n in freq[i]:
      res.append(n)
      if len(res) == k:
        return res


def tests():
  nums = [2,2,3,1,1,1]
  k = 2

  result = top_k_frequent(nums, k)
  print(result)


def driver():
  tests()
