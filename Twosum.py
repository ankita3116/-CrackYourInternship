from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for j, k in enumerate(nums):
            for x, y in enumerate(nums):
                if j != x and (k + y) == target:
                    return [j, x]  # Return the indices of the two numbers
        return []  # Return an empty list if no solution is found


nums = [2, 7, 11, 15]
target = 9

print(Solution().twoSum(nums, target))
