class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, MODIFY matrix IN PLACE
    def setZeroes(self, matrix):
        col0 = 1
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            if matrix[i][0] == 0: col0 = 0
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(m-1, -1, -1):
            for j in range(n-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0

    def setZeroes_normal(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        row = [False for i in range(m)]
        col = [False for i in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or row[j]:
                    matrix[i][j] = 0

if __name__ == '__main__':
    global matrix
    matrix = [[1, 2, 3, 4], [1, 0, 3, 5], [3, 2, 0, 7]]
    solution = Solution()
    solution.setZeroes(matrix)
    print matrix
