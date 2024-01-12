import math


def find_binary(number: int, result: str):
    if number == 0:
        return result

    result = str(number % 2) + result
    return find_binary(math.floor(number / 2), result)


def test():
    number = 233
    binary = find_binary(number, "")
    print(binary)
