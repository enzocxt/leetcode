# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def hasCycle(self, head):
        try:
            fast = head.next.next
            slow = head.next

            while fast != slow:
                fast = fast.next.next
                slow = slow.next

            return True
        except:
            return False

if __name__ == '__main__':
    A = [1, 2, 3, 1, 2, 4]
    dummy = ListNode(0)
    tmp = dummy
    for i in A:
        tmp.next = ListNode(i)
        tmp = tmp.next
    head = dummy.next
    solution = Solution()
    res = solution.hasCycle(dummy.next, 2)
    while res:
        print res.val
        res = res.next
