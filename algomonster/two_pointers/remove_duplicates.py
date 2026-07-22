def remove_duplicates(arr: list[int]) -> int:
    slow = 0

    for fast in range(len(arr)):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]
        
    return slow + 1

def driver():
    length = remove_duplicates([0, 0, 1, 1, 1, 2, 2]) # [0, 1, 2]
    print(length)