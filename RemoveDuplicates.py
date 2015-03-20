class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i, j = 0, 0
        if len(A) == 0:
            return 0
        while i < len(A):
            if A[j] != A[i]:
                A[j+1] = A[i]
                j = j+1
                i = i+1
            else:
                i = i+1

        return j + 1

if __name__ == '__main__':
    A = [1, 2, 3, 3, 4, 5, 5, 5, 6]
    solution = Solution()
    res = solution.removeDuplicates(A)
    print res
