# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next

        return head

if __name__ == '__main__':
    A = [1, 2, 2, 3, 4]
    A = [1, 1, 1]
    dummy = ListNode(0)
    tmp = dummy
    for i in A:
        tmp.next = ListNode(i)
        tmp = tmp.next
    head = dummy.next
    while head:
        print head.val
        head = head.next
    solution = Solution()
    res = solution.deleteDuplicates(dummy.next)
    while res:
        print res.val
        res = res.next
