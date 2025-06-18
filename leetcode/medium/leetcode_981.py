

class TimeMap:

  def __init__(self):
    self._hashmap = {}

  def set(self, key: str, value: str, timestamp: int) -> None:
    if key not in self._hashmap:
      self._hashmap[key] = []
    self._hashmap[key].append([value, timestamp])

  def get(self, key: str, timestamp: int) -> str:
    if key not in self._hashmap or self._hashmap[key] == []:
      return ""
    values = self._hashmap[key]
    if len(values) == 1:
      return values[0][0] if timestamp >= values[0][1] else ""
    
    # more than 1 timestamp, so now we need to search

    result = ""
    L = 0
    R = len(values) - 1

    while L <= R:
      mid = (L + R) // 2
      if values[mid][1] == timestamp:
        return values[mid][0]
      elif values[mid][1] > timestamp:
        R = mid - 1
      else:
        L = mid + 1
        result = values[mid][0]
    
    return result


def tests():
  timemap = TimeMap()
  timemap.set("foo", "bar", 1)
  print(timemap.get("foo", 1))
  print(timemap.get("foo", 3))
  timemap.set("foo", "bar2", 4)
  print(timemap.get("foo", 4))
  print(timemap.get("foo", 5))
  print(timemap.get("foo", 6))
  print(timemap.get("foo", 7))
  print(timemap.get("foo", 8))
  timemap.set("foo", "bar3", 13)
  print(timemap.get("foo", 13))


def driver():
  tests()
