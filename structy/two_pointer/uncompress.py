def uncompress(s):
    res = []
    left = 0
    right = 0
    numbers = "0123456789"

    while right < len(s):
        if s[right] in numbers:
            right += 1
        else:
            num = int(s[left:right])
            res.append(s[right] * num)
            right += 1
            left = right

    return ''.join(res)

def driver():
    res = uncompress("2c3a1t") # -> 'ccaaat'
    print(res)

    res = uncompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
    print(res)