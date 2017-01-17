## #29 Divide Two Integers
## Date: 2017.1.14

class Solution(object):
    def divide(self, dividend, divisor):
        result, is_positive = 0, True
        if dividend > 0 and divisor < 0 \
            or dividend < 0 and divisor > 0:
            is_positive = False
        if divisor == 0: return -1
        dividend, divisor = abs(dividend), abs(divisor)
        count = 0
        level4, level3, level2, level1 = 0, 0, 0, divisor
        for i in range(1000): level2 += divisor
        for i in range(1000): level3 += level2
        for i in range(1000): level4 += level3

        while dividend >= level4:
            dividend -= level4
            result += 1000000000
        while dividend >= level3:
            dividend -= level3
            result += 1000000
        while dividend >= level2:
            dividend -= level2
            result += 1000
        while dividend >= level1:
            dividend -= level1
            result += 1
        result = result if is_positive else -result
        if result >= 2147483647: return 2147483647
        elif result <= -2147483648: return -2147483648
        else: return result

print(Solution().divide(-23242341,-2))
print(divmod(-23242341,-2))
