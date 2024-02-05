# Time complexity: O(n * m * n^4)

def dfs(board, word, path, row, col, i):
    if i == len(word):
        return True

    if (row < 0 or col < 0
            or row >= len(board) or col >= len(board[0])
            or word[i] != board[row][col] or (row, col) in path):
        return False

    path.add((row, col))

    i = i + 1
    result = (
            dfs(board, word, path, row + 1, col, i) or
            dfs(board, word, path, row - 1, col, i) or
            dfs(board, word, path, row, col + 1, i) or
            dfs(board, word, path, row, col - 1, i)
    )
    path.remove((row, col))
    return result


def exists(board, word):

    rows, cols = len(board), len(board[0])
    path = set()

    for row in range(rows):
        for col in range(cols):
            if dfs(board, word, path, row, col, 0):
                return True

    return False


def solve():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"

    print("Word found: ", exists(board, word))
