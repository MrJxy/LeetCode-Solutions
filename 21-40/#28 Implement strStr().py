## #28 Implement strStr()
## Data: 2017.1.14

class Solution(object):
    def strStr(self, haystack, needle):
        needle_len = len(needle)
        for i in range(len(haystack) - needle_len + 1):
            if needle == haystack[i:i+needle_len]:
                return i
        return -1

print(Solution().strStr("1a3", "a3"))
