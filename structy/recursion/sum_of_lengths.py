def sum_of_lengths(strings: list[str]) -> int:
    if len(strings) == 0:
        return 0
    return len(strings[0]) + sum_of_lengths(strings[1:])

def driver():
    res = sum_of_lengths(['bike', 'at', 'pencils', 'phone']) # -> 18
    print(res)
