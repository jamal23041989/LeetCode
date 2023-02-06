class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x) == str(x)[::-1] else False


res = Solution()
print(res.isPalindrome(121))
print(res.isPalindrome(12))