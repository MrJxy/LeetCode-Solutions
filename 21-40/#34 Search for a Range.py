## #34 Search for a Range
## Date: 2017.1.19

class Solution(object):
    def binarySearch(self, nums, target):
        if len(nums) == 0: return [-1, -1, -1]
        if len(nums) == 1:
            return [-1, -1, -1] if nums[0] != target else [0, 0, 0]
        if len(nums) == 2:
            if nums[0] == target: return [0, 0, 1]
            elif nums[1] == target: return [1, 0, 1]
            else: return [-1, -1, -1]
        left, right = 0, len(nums) - 1
        pivot = int((left + right) / 2)
        if nums[pivot] < target:
            recur = self.binarySearch(nums[pivot:], target)
            return [-1, -1, -1] if recur == [-1, -1, -1] else list(map(lambda x: x + pivot, recur))
        elif nums[pivot] > target:
            recur = self.binarySearch(nums[:pivot], target)
            return [-1, -1, -1] if recur == [-1, -1, -1] else recur
        else :
            return [pivot, left, right]

    def searchRange(self, nums, target):
        ret_list = [-1, -1]
        bs = self.binarySearch(nums, target)
        if bs == [-1, -1, -1]: return [-1, -1]
        left = [bs[1], bs[0]]
        right = [bs[0], bs[2]]
        while left[1] - left[0] > 1:
            pivot = int((left[0] + left[1]) / 2)
            if nums[pivot] < target:
                left[0] = pivot
            else:
                left[1] = pivot
        else :
            if left[1] - left[0] == 1:
                ret_list[0] = left[0] if nums[left[0]] == target else left[1]
            else:
                ret_list[0] = left[0]
        while right[1] - right[0] > 1:
            pivot = int((right[0] + right[1]) / 2)
            if nums[pivot] > target:
                right[1] = pivot
            else:
                right[0] = pivot
        else:
            if right[1] - right[0] == 1:
                ret_list[1] = right[1] if nums[right[1]] == target else right[0]
            else:
                ret_list[1] = right[0]
        return ret_list




print(Solution().searchRange([1,2,2,3,4,4,4], 4))