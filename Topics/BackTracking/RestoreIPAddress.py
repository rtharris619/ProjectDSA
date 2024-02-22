from typing import List


def restore_ip_address(s: str) -> List[str]:
    result = []

    if len(s) > 12:
        return result

    def backtrack(i: int, dots: int, current_ip: str):
        if dots == 4 and i == len(s):
            result.append(current_ip[:-1])
            return
        if dots > 4:
            return

        for j in range(i, min(i + 3, len(s))):
            if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                backtrack(j + 1, dots + 1, current_ip + s[i:j+1] + ".")
    backtrack(0, 0, "")

    return result


def solve():
    s = "25525511135"
    result = restore_ip_address(s)
    print(result)
