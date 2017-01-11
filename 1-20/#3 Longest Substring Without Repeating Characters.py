## #3 Longest Substring Without Repeating Characters
## Date: 2017.1.11

"""
:type s: str
:rtype: int
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        for index1 in range(len(s)):
            substrlen = 0
            chset = set()
            for ch in s[index1:]:
                if ch not in chset:
                    substrlen += 1
                    chset.add(ch)
                else:
                    if substrlen > max_length: max_length = substrlen
                    break
            else: max_length = substrlen if substrlen > max_length else max_length
        return max_length

print(Solution().lengthOfLongestSubstring("c"))

