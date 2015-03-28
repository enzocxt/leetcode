# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head == None or head.next == None:
            return head
        head1 = ListNode(0)
        head2 = ListNode(0)
        p1, p2 = head1, head2
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
                p = p.next
                p1.next = None
            else:
                p2.next = p
                p2 = p2.next
                p = p.next
                p2.next = None

        p1.next = head2.next

        return head1.next

if __name__ == '__main__':
    A = [1, 2, 3, 1, 2, 4]
    dummy = ListNode(0)
    tmp = dummy
    for i in A:
        tmp.next = ListNode(i)
        tmp = tmp.next
    head = dummy.next
    solution = Solution()
    res = solution.partition(dummy.next, 3)
    while res:
        print res.val
        res = res.next
