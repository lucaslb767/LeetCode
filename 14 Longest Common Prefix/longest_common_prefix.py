class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        
        possible_patterns = {}
        longest_pattern = ""

        for i in range(len(strs[0])):
            possible_patterns[strs[0][:i+1]] = 0

        for string in strs[1:]:
            for pattern in possible_patterns:
                if pattern in string:
                    possible_patterns[pattern] += 1
                else:
                    possible_patterns[pattern] = 0
        key_common_value = 0
        for key,value in possible_patterns.items():
            if value >= key_common_value:
                key_common_value = value
                if len(key) > len(longest_pattern):
                    longest_pattern = key
        
        if possible_patterns[longest_pattern] == 0:
            longest_pattern = ""
        

        return longest_pattern
            

a = Solution()
strs = ["flower","flow","flight"]
strs2 = ["aaa","aa","aaa"]
strs3 = ["dog","racecar","car"]
print(a.longestCommonPrefix(strs))
print(a.longestCommonPrefix(strs2))
print(a.longestCommonPrefix(strs3))

