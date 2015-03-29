# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a list node
    # @param, k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head == None or head.next == None: return head

        dummy = ListNode(0)
        dummy.next = head
        p = dummy

        p1 = p
        while 1:
            for i in range(k):
                if p == None: break
                p = p.next
            if p == None: break

            p2 = p
            for i in range(k-1):
                tmp = p1.next.next
                p1.next.next = p2.next
                p2.next = p1.next
                p1.next = tmp

            for i in range(k-1):
                p2 = p2.next
            p = p2
            p1 = p

        return dummy.next

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8]
    #A = [1, 3, 6, 4, 5, 2]
    dummy = ListNode(0)
    tmp = dummy
    for i in A:
        tmp.next = ListNode(i)
        tmp = tmp.next
    solution = Solution()
    res = solution.reverseKGroup(dummy.next, 3)
    while res:
        print res.val
        res = res.next
