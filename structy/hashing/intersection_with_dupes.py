from typing import Any
from collections import Counter

def intersection_with_dupes(a: list[Any], b: list[Any]) -> list[Any]:
    count_a = Counter(a)
    count_b = Counter(b)

    result = []
    for x in count_a:
        for _ in range(0, min(count_a[x], count_b[x])):
            result.append(x)
    return result

def driver():
    a = ["q", "b", "m", "s", "s", "s"]
    b = ["s", "m", "s"]
    res = intersection_with_dupes(a, b) # -> ["m", "s", "s"]
    print(res)