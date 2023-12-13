###
# 3: Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description
###

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        sliding_window = 1
        hashmap = {}

        for i in range(len(s)):
            char = s[i]

            if char in hashmap and hashmap[char] >= sliding_window:
                sliding_window = hashmap[char] + 1
            else:
                maximum = max(maximum, i - sliding_window + 1)

            hashmap[char] = i

        return maximum


def test1():
    s = "abcabcbb"
    sol = Solution()
    ans = sol.lengthOfLongestSubstring(s)
    print(ans)


def test2():
    s = "bbbbb"
    sol = Solution()
    ans = sol.lengthOfLongestSubstring(s)
    print(ans)


def test3():
    s = "pwwkew"
    sol = Solution()
    ans = sol.lengthOfLongestSubstring(s)
    print(ans)


def solve():
    test1()
    test2()
    test3()
