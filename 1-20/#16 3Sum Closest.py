## #16 3Sum Closest
## Data: 2017.1.14

import math

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        trisum = lambda x, y, z: x + y + z
        closest = float("inf")
        if len(nums) <= 3: return sum(nums)
        for ind1 in range(len(nums) - 2):
            left = ind1 + 1
            right = len(nums) - 1
            while left < right:
                tri = trisum(nums[ind1], nums[left], nums[right])
                if abs(tri - target) < abs(closest - target):
                    closest = tri
                if tri > target: right -= 1
                elif tri < target: left += 1
                else: return target
        return closest


print(Solution().threeSumClosest([1, 1, 1, 0], 100))