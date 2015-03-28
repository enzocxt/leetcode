# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if k == 0: return head
        if head == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        count = 0
        while p.next:
            p = p.next
            count += 1
        p.next = dummy.next
        step = count - (k % count)
        for i in range(step):
            p = p.next
        head = p.next
        p.next = None

        return head

if __name__ == '__main__':
    A = [1, 2, 3, 1, 2, 4]
    dummy = ListNode(0)
    tmp = dummy
    for i in A:
        tmp.next = ListNode(i)
        tmp = tmp.next
    head = dummy.next
    solution = Solution()
    res = solution.rotateRight(dummy.next, 2)
    while res:
        print res.val
        res = res.next
