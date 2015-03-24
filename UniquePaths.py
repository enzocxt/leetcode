class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        grid = [[0 for i in range(n)] for j in range(m)]
        grid[0][0] = 1
        for j in range(1, n):
            grid[0][j] = grid[0][j-1]
        for i in range(1, m):
            grid[i][0] = grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        print grid
        return grid[m-1][n-1]

if __name__ == '__main__':
    solution = Solution()
    res = solution.uniquePaths(3, 4)
    print res
