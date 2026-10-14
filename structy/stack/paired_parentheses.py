def paired_parentheses(string):
    count = 0
    for c in string:
        if c == "(":
            count += 1
        elif c == ")":
            if count == 0:
                return False
            count -= 1
    return count == 0

def driver():
    res = paired_parentheses("(david)((abby))") # -> True
    print(res)

    res = paired_parentheses("()rose(jeff") # -> False
    print(res)

    res = paired_parentheses(")(") # -> False
    print(res)

    res = paired_parentheses("") # -> True
    print(res)

    res = paired_parentheses("))()") # False
    print(res)