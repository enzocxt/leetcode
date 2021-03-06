class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        #if m == 1 and n == 1:
        #    return grid[0][0]

        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]

        return dp[-1][-1]

if __name__ == '__main__':
    grid = [[1, 2, 3], [2, 2, 3], [3, 2, 3]]
    grid = [[1, 2, 3]]
    grid = [[1]]
    grid = [[1], [2], [3]]
    grid = [[9, 1, 4, 8]]
    solution = Solution()
    res = solution.minPathSum(grid)
    print res
