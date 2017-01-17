## #33 Search in Rotated Sorted Array
## Date: 2017.1.15

class Solution(object):
    def binarySearch(self, nums, target):
        if len(nums) == 1:
            return -1 if nums[0] != target else 0
        if len(nums) == 2:
            if nums[0] == target: return 0
            elif nums[1] == target: return 1
            else: return -1
        left, right = 0, len(nums) - 1
        pivot = int((left + right) / 2)
        if nums[pivot] < target:
            sub_bs = self.binarySearch(nums[pivot+1:], target)
            return -1 if sub_bs == -1 else pivot + sub_bs + 1
        elif nums[pivot] > target:
            sub_bs = self.binarySearch(nums[:pivot], target)
            return -1 if sub_bs == -1 else sub_bs
        else: return pivot


    def search(self, nums, target):
        if nums == []: return -1
        if len(nums) == 1:
            return -1 if nums[0] != target else 0
        if len(nums) == 2:
            if nums[0] == target: return 0
            elif nums[1] == target: return 1
            else: return -1
        if nums[0] < nums[-1]:
            return self.binarySearch(nums, target)
        else:
            left, right = 0, len(nums) -1
            pivot = int((left + right) / 2)
            if nums[pivot] >= nums[0]:
                if target >= nums[0]:
                    if target < nums[pivot]:
                        recur = self.search(nums[:pivot], target)
                        return -1 if recur == -1 else recur
                    else:
                        recur = self.search(nums[pivot:], target)
                        return -1 if recur == -1 else pivot + recur
                else:
                    recur = self.search(nums[pivot:], target)
                    return -1 if recur == -1 else pivot + recur
            else:
                if target >= nums[0]:
                    recur = self.search(nums[:pivot], target)
                    return -1 if recur == -1 else recur
                else:
                    if target < nums[pivot]:
                        recur = self.search(nums[:pivot], target)
                        return -1 if recur == -1 else recur
                    else:
                        recur = self.search(nums[pivot:], target)
                        return -1 if recur == -1 else pivot + recur



print(Solution().search([3,5,1], 1))