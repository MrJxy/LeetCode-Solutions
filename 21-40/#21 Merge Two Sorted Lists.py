## #21 Merge Two Sorted Lists
## Data: 2017.1.14

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        iter = head
        while l1 and l2:
            if l1.val <= l2.val:
                iter.next = l1
                l1 = l1.next
                iter = iter.next
            else:
                iter.next = l2
                l2 = l2.next
                iter = iter.next
        if not l1: iter.next = l2
        if not l2: iter.next = l1
        head = head.next
        return head
