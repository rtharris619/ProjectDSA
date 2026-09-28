from collections import Counter

def longest_two_char_substring(s):
    longest = 1
    start = 0
    distinct_count = 2
    window_counter = Counter()
    
    for end, leading_char in enumerate(s):
        window_counter[leading_char] += 1
        while len(window_counter) > distinct_count:
            trailing_char = s[start]
            window_counter[trailing_char] -= 1
            start += 1
            if window_counter[trailing_char] == 0:
                del window_counter[trailing_char]
        if len(window_counter) == distinct_count:
            longest = max(end - start + 1, longest)

    return longest

def driver():
    res = longest_two_char_substring("xyzyyx") # -> 4
    print(res)
    # 'yzyy' is the longest substring of 2 distinct characters and its length is 4
