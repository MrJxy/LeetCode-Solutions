## #10 Regular Expression Matching
## Data: 2017.1.13

## Have not been accepted due to TLE!
## Need to be improved by DP!

class Solution(object):
    def isMatch(self, s, p):
        if p == '': return s == ''
        if len(p) == 1:
            if p == '.': return len(s) == 1
            else: return p == s
        if p[1] != '*':
            if s == '': return False
            return (p[0] == s[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        else:
            i = 0
            while i < len(s):
                if self.isMatch(s[i:], p[2:]): return True
                if s[i] != p[0] and p[0] != '.': break

                i += 1
            return self.isMatch(s[i:], p[2:])



print(Solution().isMatch("bbbba", ".*ba"))