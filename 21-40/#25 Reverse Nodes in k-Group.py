## #25 Reverse Nodes in k-Group
## Date: 2017.1.14

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        head_setted = False
        if not head: return head
        if k <= 1: return head
        iter, prev = head, ListNode(0)
        node = []
        for i in range(k):
            if not iter: return head
            node.append(iter)
            iter = iter.next
        while node[-1]:
            temp = node[-1].next
            for i in range(1, len(node)):
                node[i].next = node[i-1]
            else: node[0].next = temp
            if not head_setted:
                head = node[-1]
                head_setted = True
            prev.next = node[-1]
            prev = node[0]
            iter = prev.next
            node.clear()
            for i in range(k):
                if not iter:
                    node.append(None)
                    break
                node.append(iter)
                iter = iter.next
        return head

test = ListNode(1)
test.next = ListNode(2)
test.next.next = ListNode(3)
test.next.next.next = ListNode(4)
print(Solution().reverseKGroup(test, 2).next.next.val)