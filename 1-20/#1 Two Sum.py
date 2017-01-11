## #1 Two Sum
## 2017.1.11

"""
:type nums: List[int]
:type target: int
:rtype: List[int]
"""

class Solution(object):
    def twoSum(self, nums, target):
        for index1,item1 in enumerate(nums):
            for index2,item2 in enumerate(nums[index1 + 1:]):
                if item1 + item2 == target: return [index1, index2 + index1 + 1]
        return []


test = Solution()
print(test.twoSum([2,7,11,15], 17))

