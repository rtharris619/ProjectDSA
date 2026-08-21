def palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])

def driver():
    res = palindrome("rotator") # -> True
    print(res)

    res = palindrome("abcbca") # -> False
    print(res)