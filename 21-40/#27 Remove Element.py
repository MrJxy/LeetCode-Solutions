## #27 Remove Element
## Date: 2017.1.14

class Solution(object):
    def removeElement(self, nums, val):
        if len(nums) == 0: return 0
        index, length = 0, len(nums)
        while index < length:
            if nums[index] == val:
                nums.pop(index)
                index -= 1
                length -= 1
            index += 1
        return length

