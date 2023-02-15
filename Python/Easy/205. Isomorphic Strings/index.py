class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = dict()
        if len(s) == 0 and len(t) == 0:
            return False

        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            else:
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]
        return True





a = Solution()
print(a.isIsomorphic(s="egg", t="add"))  # true
print(a.isIsomorphic(s="foo", t="bar"))  # false
print(a.isIsomorphic(s="paper", t="title"))  # true
