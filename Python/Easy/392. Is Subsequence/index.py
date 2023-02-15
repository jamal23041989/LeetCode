class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        return self.isSubsequence(s[1:], t[1:]) if s[0] == t[0] else self.isSubsequence(s, t[1:])


a = Solution()
print(a.isSubsequence(s="abc", t="ahbgdc"))  # true
print(a.isSubsequence(s="axc", t="ahbgdc"))  # false
print(a.isSubsequence(s="acb", t="ahbgdc"))  # false


