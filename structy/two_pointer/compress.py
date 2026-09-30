def compress(s):
    res = []
    start = 0
    end = 0
    s += "!"

    while end < len(s):
        if s[start] == s[end]:
            end += 1
        else:
            count = end - start
            if count > 1:
                res.append(str(count))
            res.append(s[start])
            start = end

    return ''.join(res)

def driver():
    res = compress('ccaaatsss') # -> '2c3at3s'
    print(res)