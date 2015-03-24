class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal_dp(self, triangle):
        n = len(triangle)
        path = [0 for i in range(n)]
        path[0] = triangle[0][0]
        for i in range(1, n):
            for j in range(len(triangle[i])-1, -1, -1):
                if j == len(triangle[i])-1:
                    path[j] = path[j-1] + triangle[i][j]
                elif j == 0:
                    path[j] = path[j] + triangle[i][j]
                else:
                    path[j] = min(path[j-1], path[j]) + triangle[i][j]

        return min(path)

    def minimumTotal(self, triangle):
        n = len(triangle)
        path = []
        for i in range(n):
            line = [0 for j in range(i+1)]
            path.append(line)

        path[0][0] = triangle[0][0]
        for i in range(1, n):
            path[i][0] = path[i-1][0] + triangle[i][0]
        for i in range(1, n):
            path[i][i] = path[i-1][i-1] + triangle[i][i]

        for i in range(1, n):
            for j in range(1, i):
                path[i][j] = min(path[i-1][j-1], path[i-1][j]) + triangle[i][j]

        print path
        res = path[n-1][0]
        for i in range(1, n):
            if res > path[n-1][i]: res = path[n-1][i]

        return res

if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    solution = Solution()
    res = solution.minimumTotal_dp(triangle)
    print res
