## #32 Longest Valid Parentheses
## Date: 2017.1.15

class Solution(object):
    def longestValidParentheses(self, s):
        stack = []
        start, max_len = 0, 0
        for i in range(len(s)):
            if s[i] == '(': stack.append(i)
            else :
                if stack == []:
                    start = i + 1
                else:
                    prev = stack.pop()
                    if stack == []:
                        length = i - start + 1
                        max_len = length if length > max_len else max_len
                    else :
                        length = i - stack[-1]
                        max_len = length if length > max_len else max_len
        return max_len

print(Solution().longestValidParentheses('(()()'))