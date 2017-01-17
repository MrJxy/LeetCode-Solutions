## #14 Longest Common Prefix
## Date: 2017.1.13

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ""
        ret = ""
        for index in range(len(strs[0])):
            for s in strs:
                if len(s) <= index or s[index] != strs[0][index]:
                    return ret
            ret += strs[0][index]
        return ret

print(Solution().longestCommonPrefix(['sss', 'ss', 'sssfd']))