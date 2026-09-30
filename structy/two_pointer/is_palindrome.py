def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

def driver():
    res = is_palindrome("rotator") # -> True
    print(res)

    res = is_palindrome("abcbca") # -> False
    print(res)

    res = is_palindrome("") # -> True
    print(res)