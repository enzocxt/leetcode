class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        left = 0
        right = len(A) - 1

        while left <= right:
            mid = (left + right) / 2
            if A[mid] < target:
                left = mid + 1
            elif A[mid] > target:
                right = mid -1
            else:
                return mid

        return left

if __name__ == '__main__':
    A = [1, 3, 5, 6]
    solution = Solution()
    res = solution.searchInsert(A, 5)
    res = solution.searchInsert(A, 2)
    res = solution.searchInsert(A, 7)
    #res = solution.searchInsert(A, 0)
    print res
