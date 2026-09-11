def has_substring_anagram(s: str, anagram: str):    
    k = len(anagram)
    window_set = set(s[:k])
    anagram_set = set(anagram)

    if window_set == anagram_set:
        return True

    for i in range(0, len(s) - k):
        window_set.remove(s[i])
        window_set.add(s[i + k])
        if window_set == anagram_set:
            return True

    return False

def driver():
    res = has_substring_anagram("greyhounds", "hoy") # -> True
    print(res)
    # the substring "yho" is an anagram of "hoy"

    res = has_substring_anagram("gruyheonds", "hoy") # -> False
    print(res)
