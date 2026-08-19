from collections import Counter

def anagrams(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    
    count: dict[str, int] = {}

    for c in s1:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    for c in s2:
        if c in count:
            count[c] -= 1
        else:
            return False
        if count[c] < 0:
            return False

    return True

def anagrams_2(s1: str, s2: str) -> bool:
    return Counter(s1) == Counter(s2)

def anagrams_3(s1: str, s2: str) -> bool:
    return counter(s1) == counter(s2)

def counter(s: str) -> dict[str, int]:
    count: dict[str, int] = {}

    for c in s:
        if c not in count:
            count[c] = 0
        count[c] += 1

    return count

def driver():
    s1 = 'restful'
    s2 = 'fluster'
    res = anagrams_3(s1, s2)
    print(res)

    s1 = 'cats'
    s2 = 'tocs'
    res = anagrams_3(s1, s2)
    print(res)