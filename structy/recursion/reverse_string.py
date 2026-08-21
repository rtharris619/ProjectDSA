def reverse_string(s: str) -> str:
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]

def driver():
    res = reverse_string("stopwatch") # -> "hctawpots"
    print(res)