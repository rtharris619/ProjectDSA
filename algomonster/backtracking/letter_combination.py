
def letter_combination(n: int) -> list[str]:
    def dfs(i: int, path: list[str]):
        if i == n:
            res.append("".join(path))
            return
        for letter in "ab":
            path.append(letter)
            dfs(i + 1, path)
            path.pop()

    res: list[str] = []
    dfs(0, [])
    return res


def driver():
    res = letter_combination(4)
    print(res)