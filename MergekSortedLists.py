# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param a list of ListNode
    # @return a ListNode
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

    def mergeKLists(self, lists):
        k = len(lists)
        lst = []

        i = 0
        while i < k/2 * 2:
            head = self.merge(lists[i], lists[i+1])
            p = head
            #while p:
            #    print p.val
            #    p = p.next
            lst.append(head)
            i += 2
        if k % 2 != 0: lst.append(lists[-1])

        if len(lst) != 1:
            self.mergeKLists(lst)

        return lst[0]


if __name__ == '__main__':
    lists = []
    A = [1, 2, 3, 4, 5, 6, 7, 8]
    B = [1, 3, 4, 5]
    C = [4, 6, 7, 8]
    d = [A, B, C]
    for i in d:
        dummy = ListNode(0)
        tmp = dummy
        for j in i:
            tmp.next = ListNode(j)
            tmp = tmp.next
        lists.append(dummy.next)
    solution = Solution()
    res = solution.mergeKLists(lists)
    while res:
        print res.val
        res = res.next
