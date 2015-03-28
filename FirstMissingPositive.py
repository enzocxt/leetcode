class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        for i in range(n):
            while A[i] > 0 and A[i] <= n and A[A[i]-1] != A[i]:
                  A[i], A[A[i]-1] = A[A[i]-1], A[i]

        for i in range(n):
            if A[i] != i+1:
                return i+1

        return n+1

if __name__ == '__main__':
    A = [3, 4, -1, 1]
    solution = Solution()
    res = solution.firstMissingPositive(A)
    print res
