from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required = dict()
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]], i]
            else:
                required[nums[i]] = i


res = Solution()
print(res.twoSum([2, 7, 11, 15], 9)) # [0,1]
print(res.twoSum([2, 11, 7, 15], 9)) # [0,2]
print(res.twoSum([3, 2, 4], 6)) # [1,2]
print(res.twoSum([3, 3], 6)) # [0,1]


