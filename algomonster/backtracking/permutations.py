def permutations(letters: str) -> list[str]:
    res: list[str] = []
    path: list[str] = []
    n = len(letters)
    used = [False] * n    

    def dfs(start: int):
        if start == n:
            res.append("".join(path))
            return

        for i, letter in enumerate(letters):
            if used[i]:
                continue
            path.append(letter)
            used[i] = True
            dfs(start + 1)
            path.pop()
            used[i] = False


    dfs(0)
    return res

def driver():
    letters = "abc"
    res = permutations(letters)
    print(res)
