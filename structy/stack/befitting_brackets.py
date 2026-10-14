def befitting_brackets(string):
    stack = []
    for char in string:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if char == ')' and last != '(':
                return False
            if char == '}' and last != '{':
                return False
            if char == ']' and last != '[':
                return False
    return len(stack) == 0

def befitting_brackets_2(string):
    stack = []
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    for char in string:
        if char in brackets:
            stack.append(brackets[char])
        else:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                return False
    return len(stack) == 0

def driver():
    res = befitting_brackets('(){}[](())') # -> True
    print(res)

    res = befitting_brackets('[][}') # -> False
    print(res)