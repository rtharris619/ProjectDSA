
def total_n_queens(n: int) -> int:
    if n == 1:
        return 1

    col = set()
    positive_diagonal = set()
    negative_diagonal = set()

    def backtrack(r: int):
        count = 0
        if r == n:
            return 1

        for c in range(n):
            if c in col or (r + c) in positive_diagonal or (r - c) in negative_diagonal:
                continue
            col.add(c)
            positive_diagonal.add(r + c)
            negative_diagonal.add(r - c)
            count += backtrack(r + 1)
            col.remove(c)
            positive_diagonal.remove(r + c)
            negative_diagonal.remove(r - c)

        return count

    result = backtrack(0)

    return result


def solve():
    n = 4
    result = total_n_queens(n)
    print(result)
