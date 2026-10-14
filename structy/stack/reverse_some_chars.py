def reverse_some_chars(s, chars):
    res = []
    stack = []
    char_set = set(chars)
    for c in s:
        if c in char_set:
            stack.append(c)
    for c in s:
        if c in char_set:
            res.append(stack.pop())
        else:
            res.append(c)
    return "".join(res)

def driver():
    res = reverse_some_chars("computer", ["a", "e", "i", "o", "u"]) # -> 'cemputor'
    # 'o', 'u', and 'e' are target characters in 'computer'
    # so their relative order should be reversed to result in 'cemputor'
    print(res)

    res = reverse_some_chars("skateboard", ["a", "e", "i", "o", "u"]) # -> 'skatobeard'
    print(res)