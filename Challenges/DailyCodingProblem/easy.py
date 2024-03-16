from typing import List


class DCP1:

    @staticmethod
    def two_sum_brute_force(nums: List[int], k: int):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                value = nums[i] + nums[j]
                if value == k:
                    print(nums[i], nums[j])
                    return True
        return False

    @staticmethod
    def two_sum(nums: List[int], k: int):
        hashmap = {}
        for i in range(len(nums)):
            if k - nums[i] in hashmap:
                return True

            hashmap[nums[i]] = True

        return False

    def solve(self):
        nums = [10, 15, 3, 7]
        k = 17
        result = self.two_sum(nums, k)
        print(result)


def driver():
    dcp = DCP1()
    dcp.solve()
