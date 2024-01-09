
def is_palindrome(input: str):

    if len(input) == 0 or len(input) == 1:
        return True

    if input[0] == input[len(input) - 1]:
        return is_palindrome(input[1:len(input) - 1])

    return False


def test():
    word = 'kayak'
    result = is_palindrome(word)
    print(result)

    word = 'racecar'
    result = is_palindrome(word)
    print(result)

    word = 'testing'
    result = is_palindrome(word)
    print(result)
