## #22 Generate Parentheses
## Date: 2017.1.14

class Solution(object):
    def generateParenthesis(self, n):
        if n == 0: return ['']
        if n == 1: return ['()']
        if n == 2: return ['()()', '(())']
        ret_list = []
        for i in range(n):
            left = self.generateParenthesis(i)
            right = self.generateParenthesis(n - 1 - i)
            handle_left = []
            handle_right = []
            for s in left: handle_left.append('(' + s + ')')
            for s in right: handle_right.append('(' + s + ')')
            for s1 in handle_left:
                for s2 in right:
                    ret_list.append(s1 + s2)
            for s1 in left:
                for s2 in handle_right:
                    ret_list.append(s1 + s2)
        ret_list = list(set(ret_list))
        return ret_list

print(Solution().generateParenthesis(4))
