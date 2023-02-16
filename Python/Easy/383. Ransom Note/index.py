class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        slv = dict()

        for x in ransomNote:
            if x in slv:
                slv[x] = slv[x] + 1
                continue
            slv[x] = 1

        for k in slv.keys():
            if magazine.count(k) < slv[k]:
                return False
        return True


a = Solution()
print(a.canConstruct("a", "b"))  # false
print(a.canConstruct("aa", "ab"))  # false
print(a.canConstruct("aa", "aab"))  # true
print(a.canConstruct("aab", "baa"))  # true
print(a.canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))  # true
print(a.canConstruct("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))  # false
