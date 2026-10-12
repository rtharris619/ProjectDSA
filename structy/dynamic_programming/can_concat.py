def can_concat(s, words):
    return _can_concat_optimised(s, words, 0, {})

def _can_concat(s, words, memo):
    if s in memo:
        return memo[s]
    if s == "":
        return True

    for word in words:
        if s.startswith(word):
            suffix = s[len(word):] # slows down a bit here because of slicing [Adds O(n) to the TC]
            if _can_concat(suffix, words, memo):
                memo[s] = True
                return True

    memo[s] = False
    return False

def _can_concat_optimised(s: str, words, i, memo):
    if i in memo:
        return memo[i]
    if i == len(s):
        return True

    for word in words:
        if s.startswith(word, i):
            if _can_concat_optimised(s, words, i + len(word), memo):
                memo[i] = True
                return True
    memo[i] = False
    return False

def driver():
    res = can_concat("oneisnone", ["one", "none", "is"]) #  -> True
    print(res)

    res = can_concat("oneisnone", ["on", "e", "is"]) #  -> False
    print(res)

    res = can_concat("santahat", ["santah", "san", "hat", "tahat"]) #  -> True
    print(res)