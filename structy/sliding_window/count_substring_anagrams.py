from collections import Counter

def count_substring_anagrams(s: str, anagram: str) -> int:
    k = len(anagram)
    window_map = Counter(s[:k])
    anagram_map = Counter(anagram)
    count = 1 if window_map == anagram_map else 0

    for i in range(0, len(s) - k):
        window_map[s[i]] -= 1
        window_map[s[i + k]] += 1        
        if window_map == anagram_map:
            count += 1

    return count

def driver():
    res = count_substring_anagrams("tacoctacabcatt", "cat") # -> 4
    print(res)
    # the 4 substrings that are an anagram of "cat" are:
    #  - tac
    #  - cta
    #  - tac
    #  - cat

    res = count_substring_anagrams("gattactat", "att") # -> 3
    print(res)