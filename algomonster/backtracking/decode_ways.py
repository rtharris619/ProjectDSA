def decode_ways(digits: str) -> int:
    def dfs(start: int) -> int:
        if start == len(digits):
            return 1
        ways = 0
        if digits[start] == "0": # can't decode string with leading zero
            return 0
        ways += dfs(start + 1) # decode 1 digit
        if 10 <= int(digits[start:start + 2]) <= 26:
            ways += dfs(start + 2) # decode 2 digits
        return ways

    return dfs(0)

def decode_ways_memo(digits: str) -> int:
    memo: dict[int, int] = {}
    def dfs(start: int) -> int:
        if start == len(digits):
            return 1
        if start in memo:
            return memo[start]
        ways = 0
        if digits[start] == "0":
            return 0
        ways += dfs(start + 1)
        if 10 <= int(digits[start:start + 2]) <= 26:
            ways += dfs(start + 2)
        memo[start] = ways
        return ways

    return dfs(0)

def driver():
    digits = "123"
    res = decode_ways_memo(digits)
    print(res)