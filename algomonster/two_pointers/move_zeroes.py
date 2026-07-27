def move_zeros(nums: list[int]) -> None:
    slow = 0
    for fast in range(len(nums)):        
        if nums[fast] > 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    print(nums)

def driver():
    nums = [1, 0, 2, 0, 0, 7]
    move_zeros(nums) # [1, 2, 7, 0, 0, 0]