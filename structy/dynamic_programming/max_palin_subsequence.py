def max_palin_subsequence(string):
    return _max_palin_subsequence(string, 0, len(string) - 1, {})

def _max_palin_subsequence(string, left, right, memo):
    key = (left, right)
    if key in memo:
        return memo[key]

    if left > right:
        return 0
    if left == right:
        return 1

    max_len = 0
    if string[left] != string[right]:
        left_side = _max_palin_subsequence(string, left + 1, right, memo)
        right_side = _max_palin_subsequence(string, left, right - 1, memo)
        max_len = max(left_side, right_side)
    else:
        shrink_res = _max_palin_subsequence(string, left + 1, right - 1, memo) + 2
        max_len = max(max_len, shrink_res)

    memo[key] = max_len
    return memo[key]

def driver():
    res = max_palin_subsequence("luwxult") # -> 5 | luwul or luxul
    print(res)

    res = max_palin_subsequence("xyzaxxzy") # -> 6
    print(res)

    res = max_palin_subsequence("lol") # -> 3
    print(res)

    res = max_palin_subsequence("enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe") # -> 31
    print(res)