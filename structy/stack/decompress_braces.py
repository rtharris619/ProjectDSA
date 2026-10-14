# 1. Keep pushing numbers and characters to the stack until closing brace.
# 2. Once closing brace is detected, run the decompress algorithm.
# 3. Now you pop elements until you run into a number. When you pop, you must prefix the popped character.
# 4. Repeat that character or set of characters that number of times.
# 5. Build up your segment string and then push that string to the stack.
# 6. If items remaining on the stack after going through each character, then you can just prefix each popped character.

def decompress_braces(string):
    stack = []
    for char in string:
        if char == "{":
            continue
        elif char == "}":
            segment = ""
            while not stack[-1].isdigit():
                prefix = stack.pop()
                segment = prefix + segment
            segment *= int(stack.pop())
            stack.append(segment)
        else:
            stack.append(char)
    return "".join(stack)

def driver():
    res = decompress_braces("2{q}3{tu}v") # -> qqtututuv 
    print(res)

    res = decompress_braces("ch3{ao}") # -> chaoaoao
    print(res)

    res = decompress_braces("2{y3{o}}s") # -> yoooyooos
    print(res)
