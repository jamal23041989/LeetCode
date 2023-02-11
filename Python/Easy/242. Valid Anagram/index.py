class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(" ".join(s).split()) == sorted(" ".join(t).split()) else False


a = Solution()
print(a.isAnagram(s="anagram", t="nagaram")) # true
print(a.isAnagram(s="rat", t="car")) # false
