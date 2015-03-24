class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        ret = [[0 for i in range(n)] for j in range(n)]

        count = 1
        for k in range(n/2):
            i = k
            for j in range(k, n-k):
                ret[i][j] = count
                count += 1

            j = n-1-k
            for i in range(k+1, n-k):
                ret[i][j] = count
                count += 1

            i = n-1-k
            for j in range(n-2-k, k-1, -1):
                ret[i][j] = count
                count += 1

            j = k
            for i in range(n-2-k, k, -1):
                ret[i][j] = count
                count += 1

        if n%2 != 0:
            ret[n/2][n/2] = count
        return ret

if __name__ == '__main__':
    solution = Solution()
    res = solution.generateMatrix(3)
    print res
