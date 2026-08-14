def partition(s: str) -> list[str]:

    def dfs(start: int, path: list[str]):
        if start == len(s):
            res.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            prefix = s[start:end]
            if is_palindrome(prefix):
                path.append(prefix)
                dfs(end, path)
                path.pop()

    res: list[str] = []
    dfs(0, [])
    return res

def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def driver():
    input = "aab"
    res = partition(input)
    print(res)