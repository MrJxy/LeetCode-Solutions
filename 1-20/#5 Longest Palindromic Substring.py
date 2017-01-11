## #5 Longest Palindromic Substring
## Data: 2017.1.11

"""
:type s: str
:rtype: str
"""

# class Solution(object):
#     def longestPalindrome(self, s):
#         max_length = 0
#         max_str = ""
#         for index1 in range(len(s)):
#             for index2 in range(len(s[index1:]) + 1):
#                 substr = s[index1: index1 + index2]
#                 revstr = substr[::-1]
#                 if substr == revstr and max_length < len(substr):
#                     max_length = len(substr)
#                     max_str = substr
#         return max_str
#
# print(Solution().longestPalindrome("abbb"))

class Solution(object):
    def longestPalindrome(self, s):
        max_length, max_substr = 0, ""
        for index in range(len(s)):
            #odd length of substr
            left, right = index - 1, index + 1
            plen = 1
            while left >=0 and right < len(s) and s[left] == s[right]:
                plen += 2; left -= 1; right += 1
            if plen > max_length:
                max_length, max_substr = plen, s[left+1:right]
            #even length of substr
            left, right = index, index + 1
            plen = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                plen += 2; left -= 1; right += 1
            if plen > max_length:
                max_length, max_substr = plen, s[left+1:right]
        return max_substr

print(Solution().longestPalindrome("aadda"))