## #26 Remove Duplicates from Sorted Array
## Date: 2017.1.14

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0: return 0
        length = len(nums)
        index = 1
        key = nums[0]
        while index < length:
            if nums[index] == key:
                nums.pop(index)
                index, length = index - 1, length - 1
            key = nums[index]
            index += 1
        print(nums)
        return len(nums)

print(Solution().removeDuplicates([1,2,2,3,3,4,5,5,6]))