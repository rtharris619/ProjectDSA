from collections import Counter

def longest_unique_substring(s):
    longest = 1
    start = 0
    window_counter = Counter()

    for end in range(0, len(s)):
        leading_char = s[end]
        window_counter[leading_char] += 1

        while window_counter[leading_char] > 1:
            trailing_char = s[start]
            window_counter[trailing_char] -= 1
            start += 1

        longest = max(end - start + 1, longest)

    return longest

def driver():
    res = longest_unique_substring("abcabcqbb") # -> 4
    print(res)
    # 'abcq' is the longest substring with unique characters and its length is 4
