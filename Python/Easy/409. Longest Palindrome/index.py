class Solution:
    def longestPalindrome(self, s):
        store_dic = dict()

        for single_str in s:
            if single_str in store_dic:
                del store_dic[single_str]
            else:
                store_dic[single_str] = 1

        if len(store_dic) == 0:
            return len(s) - len(store_dic)
        else:
            return len(s) - len(store_dic) + 1

a = Solution()
print(a.longestPalindrome("abccccdd"))  # 7
print(a.longestPalindrome("a"))  # 1
print(a.longestPalindrome("ccc"))  # 3



