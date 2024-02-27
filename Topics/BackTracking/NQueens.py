

def solve():
    n = 4
    col = set()
    positive_diagonal = set() # (r + c)
    negative_diagonal = set() # (r - c)

    result = []
    board = [["."] * n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return

        for c in range(n):
            if c in col or (r + c) in positive_diagonal or (r - c) in negative_diagonal:
                continue

            col.add(c)
            positive_diagonal.add(r + c)
            negative_diagonal.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            positive_diagonal.remove(r + c)
            negative_diagonal.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    print(result)
