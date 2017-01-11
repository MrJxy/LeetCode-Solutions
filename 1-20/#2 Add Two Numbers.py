## #1 Add Two Numbers
## 2017.1.11

"""
:type l1: ListNode
:type l2: ListNode
:rtype: ListNode
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ret_list = ListNode(0)
        iter = ret_list
        flag = False
        while l1 or l2:
            temp = ListNode(0)
            if not l1 : l1 = ListNode(0)
            if not l2 : l2 = ListNode(0)
            if flag:
                temp.val = (l1.val + l2.val + 1) % 10
                flag = True if l1.val + l2.val + 1 >= 10 else False
            else:
                temp.val = (l1.val + l2.val) % 10
                flag = True if l1.val + l2.val >= 10 else False
            iter.next = temp
            iter = iter.next
            l1 = l1.next
            l2 = l2.next
        else:
            if flag:
                temp = ListNode(1)
                iter.next = temp
                iter = iter.next

        ret_list = ret_list.next
        return ret_list



"""
class Solution:
# @return a ListNode
def addTwoNumbers(self, l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next
"""

