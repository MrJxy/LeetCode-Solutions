## #15 3Sum
## Data: 2017.1.13

class Solution(object):
    def threeSum(self, nums):
        solution_set = []
        neg, zero, pos = [], [], []
        for i in nums:
            if i < 0: neg.append(i)
            elif i > 0: pos.append(i)
            else: zero.append(i)
        if len(zero) >= 3: solution_set.append([0, 0, 0])
        for n in neg:
            buff_dict = dict()
            for p in pos:
                if p == -n and zero != []: solution_set.append([n, 0, p])
                if p in buff_dict:
                    solution_set.append([n, p, buff_dict[p]])
                else:
                    buff_dict[-n - p] = p
        for p in pos:
            buff_dict = dict()
            for n in neg:
                if n in buff_dict:
                    solution_set.append([n, buff_dict[n], p])
                else:
                    buff_dict[-p - n] = n
        new_set = []
        for i in solution_set:
            if i not in new_set:
                new_set.append(i)
        return new_set

print(Solution().threeSum([0, 0, 0]))

# My Another Solution
# Can be adapted to solve problems with any target
#
# class Solution(object):
#     def threeSum(self, nums):
#         nums.sort()
#         if len(nums) < 3: return []
#         solutions = []
#         for index in range(len(nums) - 2):
#             left, right = index + 1, len(nums) - 1
#             while (left < right):
#                 if nums[index] + nums[left] + nums[right] == 0:
#                     solutions.append([nums[index], nums[left], nums[right]])
#                     left += 1
#                 elif nums[index] + nums[left] + nums[right] > 0:
#                     right -= 1
#                 else:
#                     left += 1
#         new_set = []
#         for i in solutions:
#             if i not in new_set:
#                 new_set.append(i)
#         return new_set