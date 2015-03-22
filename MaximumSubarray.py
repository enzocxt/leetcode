class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        thisSum = 0
        maxSum = -10000

        for i in range(len(A)):
            if thisSum < 0:
                thisSum = 0
            thisSum = thisSum + A[i]
            maxSum = max(thisSum, maxSum)

        return maxSum

if __name__ == '__main__':
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    res = solution.maxSubArray(A)
    print res
