from typing import List


def is_palindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1

    return True


def partition(s: str) -> List[List[str]]:
    result = []
    part = []

    def dfs(i):
        if i >= len(s):
            result.append(part[:])
            return

        for j in range(i, len(s)):
            if is_palindrome(s, i, j):
                part.append(s[i:j+1])
                dfs(j + 1)
                part.pop()

    dfs(0)
    return result


def solve():
    s = "aab"
    result = partition(s)
    print(result)
