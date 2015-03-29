# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a list node
    # @return a tree node
    def merge(self, head1, head2):
        if head1 == None: return head2
        if head2 == None: return head1

        dummy = ListNode(0)
        p = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                p.next = head1
                p = p.next
                head1 = head1.next
            else:
                p.next = head2
                p = p.next
                head2 = head2.next

        if head1 == None: p.next = head2
        if head2 == None: p.next = head1

        return dummy.next

    def sortList(self, head):
        if head == None or head.next == None:
            return head

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        head = self.merge(head1, head2)

        return head

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6]
    A = [1, 3, 6, 4, 5, 2]
    dummy = ListNode(0)
    tmp = dummy
    for i in A:
        tmp.next = ListNode(i)
        tmp = tmp.next
    solution = Solution()
    res = solution.sortList(dummy.next)
    while res:
        print res.val
        res = res.next
