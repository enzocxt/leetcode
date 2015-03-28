# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        # break linked list into two equal length
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        # reverse linked list head2
        dummy = ListNode(0)
        dummy.next = head2
        p = head2.next
        head2.next = None
        while p:
            tmp = p; p = p.next
            tmp.next = dummy.next
            dummy.next = tmp
        head2 = dummy.next

        # merge two linked lists
        # head1: 1 -> 2 -> 3
        # head2: 7 -> 6 -> 5 -> 4
        p1 = head1; p2 = head2
        while p2:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7]
    dummy = ListNode(0)
    tmp = dummy
    for i in A:
        tmp.next = ListNode(i)
        tmp = tmp.next
    head = dummy.next
    solution = Solution()
    res = solution.reorderList(head)
    count = 3
    while res:
        print res.val
        res = res.next
