
def letter_combinations_of_phone_number(digits: str) -> list[str]:
    pad = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def dfs(i: int, path: list[str]):
        if i == len(digits):
            res.append("".join(path))
            return

        for letter in pad[digits[i]]:
            path.append(letter)
            dfs(i + 1, path)
            path.pop()

    res: list[str] = []
    dfs(0, [])
    return res

def driver():
    input = "235"
    res = letter_combinations_of_phone_number(input)
    print(res)