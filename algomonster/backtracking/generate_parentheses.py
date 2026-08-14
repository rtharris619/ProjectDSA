def generate_parentheses(n: int) -> list[str]:
    res: list[str] = []
    path: list[str] = []

    def dfs(start: int, open_count: int, closed_count: int):
        if start == 2 * n:
            res.append("".join(path))
            return
        if open_count < n:
            path.append("(")
            dfs(start+1, open_count+1, closed_count)
            path.pop()
        if closed_count < open_count:
            path.append(")")
            dfs(start+1, open_count, closed_count+1)
            path.pop()

    dfs(0, 0, 0)
    return res

def driver():
    n = 3
    res = generate_parentheses(n)
    print(res)