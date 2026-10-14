def running_sum(numbers):
    res = []
    total = 0
    for num in numbers:
        total += num
        res.append(total)
    return res

def driver():
    res = running_sum([4, 2, 1, 6, 3, 6]) # -> [ 4, 6, 7, 13, 16, 22 ] 
    print(res)

    res = running_sum([10, 5, -2, 1, 1]) # -> [ 10, 15, 13, 14, 15 ] 
    print(res)
