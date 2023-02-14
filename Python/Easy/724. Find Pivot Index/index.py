from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0 and 0 == sum(nums[1:]):
                return i
            elif i == len(nums) - 1 and 0 == sum(nums[:len(nums) - 1]):
                return i
            elif sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1


a = Solution()
print(a.pivotIndex([1, 7, 3, 6, 5, 6]))  # 3
print(a.pivotIndex([1, 2, 3]))  # -1
print(a.pivotIndex([2, 1, -1]))  # 0
print(a.pivotIndex([-1, -1, 0, 0, -1, -1]))  # 2
