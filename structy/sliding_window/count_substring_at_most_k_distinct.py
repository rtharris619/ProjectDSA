from collections import Counter

def count_substring_at_most_k_distinct(s, k):
    count = 0
    start = 0
    window_chars = Counter()

    for end, leading_char in enumerate(s):
        window_chars[leading_char] += 1
        while len(window_chars) > k and start <= end:
            trailing_char = s[start]
            window_chars[trailing_char] -= 1
            if window_chars[trailing_char] == 0:
                del window_chars[trailing_char]
            start += 1
        count += end - start + 1

    return count

def driver():
    res = count_substring_at_most_k_distinct("gattc", 3) # -> 14
    print(res)
    # there are 14 substrings that consist of at most 3 distinct chars:
    #   gatt
    #   attc
    #   gat
    #   att
    #   ttc
    #   ga
    #   at
    #   tt
    #   tc
    #   g
    #   a
    #   t
    #   t
    #   c
