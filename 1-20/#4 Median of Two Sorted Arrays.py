## #4 Median of Two Sorted Arrays
## Data: 2017.1.11

"""
:type nums1: List[int]
:type nums2: List[int]
:rtype: float
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merge_list = []
        iter1 = iter2 = 0
        while len(nums1) or len(nums2):
            if not len(nums1): merge_list += nums2; break
            if not len(nums2): merge_list += nums1; break
            if nums1[0] <= nums2[0]:
                merge_list.append(nums1[0])
                nums1.pop(0)
            else:
                merge_list.append(nums2[0])
                nums2.pop(0)
        print(merge_list)
        length = len(merge_list)
        #if length % 2: return merge_list[int((length - 1) / 2)]
        #else: return (merge_list[int(length/2)] + merge_list[int(length/2) - 1])/2
        if length % 2 == 0:
            index1, index2 = int(length/2), int(length/2-1)
            return (float(merge_list[index1]) + float(merge_list[index2])) / 2
        else:
            index = int((length - 1) / 2)
            return merge_list[index]



print(Solution().findMedianSortedArrays([1,2], [3,4]))
