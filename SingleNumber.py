class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ret = A[0]
        for i in range(1, len(A)):
            ret = ret ^ A[i]

        return ret

if __name__ == '__main__':
    A = [1, 2, 2, 1, 3, 4, 4]
    solution = Solution()
    res = solution.singleNumber(A)
    print res
