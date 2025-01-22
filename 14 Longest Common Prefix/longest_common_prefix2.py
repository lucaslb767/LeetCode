class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
    
a = Solution()
strs = ["flower","flow","flight"]
strs2 = ["aaa","aa","aaa"]
strs3 = ["dog","racecar","car"]
print(a.longestCommonPrefix(strs))
print(a.longestCommonPrefix(strs2))
print(a.longestCommonPrefix(strs3))