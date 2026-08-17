def word_break(s: str, words: list[str]) -> bool:
    def dfs(start: int):
        if start == len(s):
            return True
        res = False
        for word in words:
            if s[start:].startswith(word):
                res = res or dfs(start + len(word))

        return res
    return dfs(0)

def word_break_memo(s: str, words: list[str]) -> bool:
    memo: dict[int, bool] = {}
    def dfs(start: int):
        if start in memo:
            return memo[start]
        if start == len(s):
            return True
        res = False
        for word in words:
            if s[start:].startswith(word):
                if dfs(start + len(word)):
                    res = True
                    break
        memo[start] = res
        return res
    return dfs(0)

def driver():
    target = "algomonster"
    words = ["algo", "monster"]
    res = word_break_memo(target, words)
    print(res)
