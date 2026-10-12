from math import inf

def quickest_concat(s, words):
    res = _quickest_concat(s, words, 0, {})
    return -1 if res == inf else res

def _quickest_concat(s, words, i, memo):
    if i in memo:
        return memo[i]
    if i == len(s):
        return 0

    quickest = inf
    for word in words:
        if s.startswith(word, i):
            attempt = 1 + _quickest_concat(s, words, i + len(word), memo)
            quickest = min(quickest, attempt)
    memo[i] = quickest
    return quickest

def driver():
    res = quickest_concat('caution', ['ca', 'ion', 'caut', 'ut']) # -> 2
    print(res)

    res = quickest_concat('simchacindy', ['sim', 'simcha', 'acindy']) # -> -1
    print(res)