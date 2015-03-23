class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a boolean
    def search(self, A, target):
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if A[mid] == target:
                return True
            if A[mid] == A[left] == A[right]:
                left += 1
                right -= 1
            elif A[left] <= A[mid]:
                if target < A[mid] and target >= A[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > A[mid] and target <= A[right]:
                    left = mid + 1
                else:
                    right = mid -1

        return False

if __name__ == '__main__':
    A = [4, 5, 6, 6, 7, 0, 1, 1, 2]
    solution = Solution()
    res = solution.search(A, 3)
    print res
