## #19 Remove Nth Node From End of List
## Data: 2017.1.14

## Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        count, iter = 0, head
        while iter:
            iter = iter.next
            count += 1
        n = count - n + 1
        if n <= 0: return head
        if n == 1:
            head = head.next
            return head
        prev, curr = head, head
        while n > 2 and prev.next:
            prev = prev.next
            n -= 1
        curr = prev.next
        if not prev or not curr: return head
        prev.next = curr.next
        return head
