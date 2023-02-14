from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # lst = []
        # for i in range(1, len(nums)+1):
        #     lst.append(sum(nums[:i]))
        # return lst
        return [sum(nums[:i]) for i in range(1, len(nums)+1)]


a = Solution()
print(a.runningSum([1, 2, 3, 4]))  # [1,3,6,10]
print(a.runningSum([1, 1, 1, 1, 1]))  # [1,2,3,4,5]
print(a.runningSum([3, 1, 2, 10, 1]))  # [3,4,6,16,17]
