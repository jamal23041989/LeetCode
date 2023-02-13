from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if nums.count(target) > 0 else -1


a = Solution()
print(a.search([-1, 0, 3, 5, 9, 12], 9))  # 9 exists in nums and its index is 4
print(a.search([-1, 0, 3, 5, 9, 12], 2))  # 2 does not exist in nums so return -1
