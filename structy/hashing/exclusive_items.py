def exclusive_items(a: list[int], b: list[int]) -> list[int]:
    set_a = set(a)
    set_b = set(b)

    result = [item for item in a if item not in set_b]
    result.extend([item for item in b if item not in set_a])
    return result

def driver():
    a = [4,2,1,6]
    b = [3,6,9,2,10]
    res = exclusive_items(a, b) # -> [4,1,3,9,10]
    print(res)