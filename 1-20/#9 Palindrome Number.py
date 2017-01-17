## #9 Palindrome Number
## Date: 2017.1.13

class Solution(object):
    def isPalindrome(self, x):
        is_positive = True if x >= 0 else False
        x = abs(x)
        x_str = str(x)
        rev_str = x_str[::-1]
        x_rev = int(rev_str) if is_positive else -int(rev_str)
        return x_rev == x

