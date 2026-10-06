def search_row(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return True
    return False

def search_sorted_grid(grid, target):
    # search for the row
    left = 0
    right = len(grid) - 1
    while left <= right:
        mid = (left + right) // 2
        if target >= grid[mid][0] and target <= grid[mid][len(grid[0]) - 1]:
            return search_row(grid[mid], target) # search for the col
        elif target < grid[mid][0]:
            right = mid - 1
        else:
            left = mid + 1
    return False

def driver():
    grid = [
        [2,3,4,5],
        [11,12,12,15],
        [17,20,23,25],
        [30,31,32,50],
    ]
    res = search_sorted_grid(grid, 12) # -> True
    print(res)

    grid = [
        [2,3,4,5],
        [11,12,12,15],
        [17,20,23,25],
        [30,31,32,50],
    ]
    res = search_sorted_grid(grid, 21) # -> False
    print(res)

    grid = [
        [12,13,20,22,24],
        [26,27,29,30,33],
        [36,40,45,46,48],
        [54,55,60,67,70],
        [71,72,74,76,79],
        [85,87,90,92,98],
    ]
    res = search_sorted_grid(grid, 71) # -> True
    print(res)