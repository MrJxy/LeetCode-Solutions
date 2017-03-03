## #35 Search Insert Position
# Date: 2017.1.19

class Solution(object):
    def searchInsert(self, nums, target):
        if len(nums) == 0: return 0
        if len(nums) == 1:
            if nums[0] >= target: return 0
            else: return 1
        if len(nums) == 2:
            if nums[0] >= target: return 0
            elif nums[1] >= target: return 1
            else: return 2
        left, right = 0, len(nums) - 1
        pivot = int((left + right) / 2)
        if nums[pivot] < target:
            sub_bs = self.searchInsert(nums[pivot:], target)
            return -1 if sub_bs == -1 else pivot + sub_bs
        elif nums[pivot] > target:
            sub_bs = self.searchInsert(nums[:pivot], target)
            return -1 if sub_bs == -1 else sub_bs
        else: return pivot

print(Solution().searchInsert([1,3,5,6], 0))