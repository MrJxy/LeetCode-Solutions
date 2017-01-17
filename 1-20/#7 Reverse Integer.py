## #7 Reverse Integer
## Data: 2017.1.13

class Solution(object):
    def reverse(self, x):
        is_positive = True if x >= 0 else False
        x = abs(x)
        strnum = str(x)
        revstrnum = strnum[::-1]
        retnum = int(revstrnum)
        retnum = retnum if is_positive else -retnum
        retnum = 0 if retnum > 2147483647 \
            or retnum < -2147483648 else retnum
        return retnum

print(Solution().reverse(1534236469))