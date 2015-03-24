class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        path = [[0 for j in range(n)] for i in range(m)]
        path[0][0] = 1

        print path
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    if obstacleGrid[i][j-1] == 1: path[i][j] = 0
                    else: path[i][j] = path[i][j-1]
                elif j == 0 and i > 0:
                    if obstacleGrid[i-1][j] == 1: path[i][j] = 0
                    else: path[i][j] = path[i-1][j]
                elif i > 0 and j > 0:
                    if obstacleGrid[i-1][j] == 1 and obstacleGrid[i][j-1] == 0:
                        path[i][j] = path[i][j-1]
                    elif obstacleGrid[i][j-1] == 1 and obstacleGrid[i-1][j] == 0:
                        path[i][j] = path[i-1][j]
                    elif obstacleGrid[i][j-1] == 0 and obstacleGrid[i-1][j] == 0:
                        path[i][j] = path[i][j-1] + path[i-1][j]
                    else:
                        path[i][j] = 0

        print path
        return path[m-1][n-1]

if __name__ == '__main__':
    A = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    solution = Solution()
    res = solution.uniquePathsWithObstacles(A)
    print res
