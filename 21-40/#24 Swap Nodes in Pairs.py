## #24 Swap Nodes in Pairs
# Date: 2017.1.14

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        head_setted = False
        if head == None: return head
        node1, node2 = head, head.next
        prev = ListNode(0)
        while node1 and node2:
            temp = node2.next
            node2.next = node1
            node1.next = temp
            if not head_setted:
                head = node2
                head_setted = True
            prev.next = node2
            prev = node1
            node1 = node1.next
            if node1:
                node2 = node1.next
        return head

test = ListNode(1)
test.next = ListNode(2)
test.next.next = ListNode(3)
print(Solution().swapPairs(test).next.next.val)