## #18 4Sum
## Data: 2017.1.14

class Solution(object):
    def threeSum(self, nums, target):
        if len(nums) < 3: return []
        solutions = []
        for index in range(len(nums) - 2):
            left, right = index + 1, len(nums) - 1
            while(left < right):
                if nums[index] + nums[left] + nums[right] == target:
                    solutions.append([nums[index], nums[left], nums[right]])
                    left += 1
                elif nums[index] + nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return solutions

    def fourSum(self, nums, target):
        if len(nums) < 4: return []
        solutions = []
        nums.sort()
        for ind in range(len(nums) - 3):
            trisum = self.threeSum(nums[ind + 1:], target-nums[ind])
            # for l in trisum:
            #     l.insert(0, nums[ind])
            solutions += [[nums[ind]] + l for l in trisum]
        ret_solu = []
        for l in solutions:
            if l not in ret_solu:
                ret_solu.append(l)
        return ret_solu

print(Solution().fourSum([1,2, -1, -2], 0))