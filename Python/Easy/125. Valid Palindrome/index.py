class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i for i in s if i.isalnum()).lower()
        return s == s[::-1]


a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama")) # true
print(a.isPalindrome("race a car")) # false
print(a.isPalindrome(" "))  # true
print(a.isPalindrome("0P"))  # false
print(a.isPalindrome("."))  # true
print(a.isPalindrome("a"))  # true
print(a.isPalindrome("a."))  # true
print(a.isPalindrome(".,"))  # true

