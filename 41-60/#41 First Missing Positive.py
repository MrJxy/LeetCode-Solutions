## #41 First Missing Positive
## Date: 2017.2.26

class Solution(object):
    def firstMissingPositive(self, nums):
        arr = [False] * 10000
        for i in nums:
            if i > 0 and i < 10000: arr[i] = True
        for i in range(1, 10000):
            if not arr[i]: return i

print(Solution().firstMissingPositive([]))