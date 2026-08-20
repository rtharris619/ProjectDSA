def intersection(a: list[int], b: list[int]) -> list[int]:
    a_set = set(a)
    res = []
    for num in b:
        if num in a_set:
            res.append(num)
    return res

def intersection_2(a: list[int], b: list[int]) -> list[int]:
    a_set = set(a)
    return [item for item in b if item in a_set]

def driver():
    a = [4,2,1,6]
    b = [3,6,9,2,10]
    res = intersection_2(a, b)
    print(res) # -> [2,6]