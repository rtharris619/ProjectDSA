# Write a function, nesting_score, that takes in a string of brackets as an argument. 
# The function should return the score of the string according to the following rules:

# [] is worth 1 point
# XY is worth X + Y points where X, Y are substrings of well-formed brackets
# [S] is worth S * 2 points where S is a substring of well-formed brackets
# For example:

# [[][][]] is equivalent to (1 + 1 + 1) * 2 = 6

# You may assume that the input only contains well-formed square brackets.

# Algorithm
# 1. Add a 0 to the stack.
# 2. If char is an opening brace, append a 0 to the stack.
# 3. If char is a closing brace, pop from the stack and if you just popped a 0 you just add a 1 to the next item in the stack. (effectively popping twice)
# 4. If for step 3 you pop off a number greater than 0, then you must multiply current by 2 and then you add that result to the next item in the stack. (effectively popping twice)

def nesting_score(string):
    stack = [0]
    for char in string:
        if char == "[":
            stack.append(0)
        else:
            cur = stack.pop()
            if cur == 0:
                stack.append(stack.pop() + 1)
            else:
                stack.append((cur * 2) + stack.pop())
    return stack[0]

def nesting_score_2(string):
    stack = [0]
    for char in string:
        if char == "[":
            stack.append(0)
        else:
            cur = stack.pop()
            if cur == 0:
                stack[-1] += 1
            else:
                stack[-1] += 2 * cur
    return stack[0]

def driver():
    res = nesting_score_2("[]") # -> 1
    print(res)

    res = nesting_score_2("[][][]") # -> 3
    print(res)

    res = nesting_score_2("[[[[[[[][]]]]]]][]") # -> 129
    print(res)