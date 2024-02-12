

def split_string(s: str) -> bool:

    def dfs(index, prev):
        if index == len(s):
            return True

        for j in range(index, len(s)):
            outer_val = int(s[index:j+1])
            if outer_val + 1 == prev and dfs(j + 1, outer_val):
                return True

        return False

    for i in range(len(s) - 1):
        val = int(s[:i + 1])
        if dfs(i + 1, val):
            return True

    return False


def solve():
    s = "00090089"
    result = split_string(s)
    print(result)
