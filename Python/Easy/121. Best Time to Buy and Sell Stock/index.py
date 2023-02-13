from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_price = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                max_price = max(max_price, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return max_price


a = Solution()
print(a.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(a.maxProfit([7, 6, 4, 3, 1]))  # 0
print(a.maxProfit([[2, 4, 1]]))  # 2



