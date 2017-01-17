## #23 Merge k Sorted Lists
## Date: 2017.1.14

import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        heapq.heapify(heap)
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        merge_list = ListNode(0)
        iter = merge_list
        heapsize = len(heap)
        for i in range(heapsize):
            iter.next = ListNode(heapq.heappop(heap))
            iter = iter.next
        return merge_list.next

a = ListNode(3)
b = ListNode(5)
c = ListNode(0)
d = ListNode(4)
l = [a, b, c, d]
print(Solution().mergeKLists(l).next.val)