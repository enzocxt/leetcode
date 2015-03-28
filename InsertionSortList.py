# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy.next

        while curr.next:
            if curr.next.val < curr.val:
                pre = dummy
                while pre.next.val < curr.next.val:
                    pre = pre.next
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next

        return dummy.next

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
