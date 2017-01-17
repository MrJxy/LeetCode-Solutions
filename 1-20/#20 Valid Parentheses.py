## #20 Valid Parentheses
## Date: 2017.1.14

class Solution(object):
    def isValid(self, s):
        stack = []
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            elif ch == ')' and (len(stack) <= 0 or stack.pop() != '(') \
                or ch == ']' and (len(stack) <= 0 or stack.pop() != '[') \
                or ch == '}' and (len(stack) <= 0 or stack.pop() != '{'):
                return False
        if len(stack) > 0: return False
        return True

print(Solution().isValid("("))