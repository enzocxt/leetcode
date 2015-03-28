# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param two ListNode
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        lenA, lenB = 0, 0
        while curA:
            lenA += 1
            curA = curA.next
        while curB:
            lenB += 1
            curB = curB.next
        curA, curB = headA, headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB - lenA):
                curB = curB.next

        while curB != curA:
            curB = curB.next
            curA = curA.next

        return curA

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
