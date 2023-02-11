from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True


a = Solution()
print(a.containsDuplicate([1, 2, 3, 1])) # true
print(a.containsDuplicate([1, 2, 3, 4])) # false
print(a.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])) # true
