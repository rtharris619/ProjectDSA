def max_ones_with_single_flip(s):
    longest = 0
    zero_count = 0
    start = 0

    for end, leading_char in enumerate(s):
        if leading_char == "0":
            zero_count += 1
        while zero_count > 1:
            trailing_char = s[start]
            if trailing_char == "0":
                zero_count -= 1
            start += 1
        longest = max(longest, end - start + 1)

    return longest

def driver():
    res = max_ones_with_single_flip("10110110") # -> 5
    print(res)
    # flipping the second 0 will give us the longest streak of 1s

    res = max_ones_with_single_flip("011101101111") # -> 7
    print(res)

    res = max_ones_with_single_flip("10110111011110111011111") # -> 9
    print(res)

    res = max_ones_with_single_flip("111") # -> 3
    print(res)
