class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

        return matrix

    def rotate_bad(self, matrix):
        n = len(matrix)
        ret = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                ret[j][n-1-i] = matrix[i][j]

        return ret

if __name__ == '__main__':
    matrix = [[1, 2, 3], [3, 2, 1], [3, 1, 2]]
    solution = Solution()
    res = solution.rotate(matrix)
    print res
