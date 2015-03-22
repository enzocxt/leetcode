class Solution:
    # @param num, a list of integers
    # @return an integer
    def findPeakElement(self, num):
        return self.search(num, 0, len(num)-1)

    def search(self, num, start, end):
        if start == end:
            return start
        if start + 1 == end:
            return [start, end][num[start] < num[end]]

        mid = (start + end) / 2
        if num[mid] < num[mid-1]:
            return self.search(num, start, mid-1)
        if num[mid] < num[mid+1]:
            return self.search(num, mid+1, end)

        return mid

    def findPeakElement_On(self, num):
        size = len(num)
        if len(num) <= 1: return 0
        if num[0] > num[1]: return 0
        if num[size-1] > num[size-2]: return 0

        for i in range(1, size-1):
            if num[i]>num[i-1] and num[i]>num[i+1]:
                return i

if __name__ == '__main__':
    A = [1, 2, 3, 1]
    solution = Solution()
    res = solution.findPeakElement(A)
    print res
