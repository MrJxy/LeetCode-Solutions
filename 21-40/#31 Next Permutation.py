## #31 Next Permutation
## Date: 2017.1.15

class Solution(object):
    def nextPermutation(self, nums):
        if len(nums) <= 1: return
        index = len(nums) - 1
        while index > 0 and nums[index] <= nums[index - 1]:
            index -= 1
        else: index -= 1
        if index == -1: nums.sort(); return
        min_ind, min_val = 2147483648, 2147483648
        for i in range(len(nums) - 1, index, -1):
            if nums[i] < min_val and nums[i] > nums[index]:
                min_ind, min_val = i, nums[i]
        temp = nums[index]
        nums[index] = min_val
        nums[min_ind] = temp
        nums[index+1:] = sorted(nums[index+1:])

print(Solution().nextPermutation([5,3,2,1]))