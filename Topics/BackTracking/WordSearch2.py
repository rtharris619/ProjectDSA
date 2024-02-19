from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True


def find_words(board: List[List[str]], words: List[str]) -> List[str]:

    result = set()
    visited = set()

    root = TrieNode()
    for w in words:
        root.add_word(w)

    def dfs(row, col, node, word):
        if (row < 0 or col < 0 or row >= len(board) or col >= len(board[0])
                or (row, col) in visited or board[row][col] not in node.children):
            return

        visited.add((row, col))
        node = node.children[board[row][col]]
        word += board[row][col]
        if node.is_word:
            result.add(word)

        dfs(row + 1, col, node, word)
        dfs(row - 1, col, node, word)
        dfs(row, col + 1, node, word)
        dfs(row, col - 1, node, word)

        visited.remove((row, col))

    for r in range(len(board)):
        for c in range(len(board[0])):
            dfs(r, c, root, "")

    return list(result)


def solve():
    board = [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r']]
    words = ['oath', 'pea', 'eat', 'rain']

    result = find_words(board, words)
    print(result)
