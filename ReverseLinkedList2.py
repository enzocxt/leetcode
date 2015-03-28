# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy

        for i in range(m-1):
            p1 = p1.next
        for j in range(n):
            p2 = p2.next

        print p1.val, p2.val

        #while p1.next != p2.next:
        for i in range(n-m):
            print "p1, p2: %s, %s" % (p1.val, p2.val)
            tmp1 = p1.next.next
            p1.next.next = p2.next
            p2.next = p1.next
            p1.next = tmp1
            print "p1, p1.next: %s, %s" % (p1.val, p1.next.val)
            print "p2, p2.next: %s, %s" % (p2.val, p2.next.val)

        print head.val, head.next.val, head.next.next.val, head.next.next.next.val

        return dummy.next

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7]
    dummy = ListNode(0)
    tmp = dummy
    for i in A:
        tmp.next = ListNode(i)
        tmp = tmp.next
    head = dummy.next
    solution = Solution()
    res = solution.reverseBetween(head, 2, 4)
    while res:
        print res.val
        res = res.next
