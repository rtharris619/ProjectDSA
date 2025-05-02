def check_if_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


def driver():
    s = "racecar"
    result = check_if_palindrome(s)
    print(f"Is '{s}' a palindrome? {result}")
