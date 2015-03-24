class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])

        list = []
        for k in range(m/2 + 1):
            i = k
            if len(list) == m*n: break
            for j in range(k, n-k):
                list.append(matrix[i][j])

            if len(list) == m*n: break
            j = n-1-k
            for i in range(k+1, m-k):
                if len(list) == m*n: break
                list.append(matrix[i][j])

            if len(list) == m*n: break
            i = m-1-k
            for j in range(n-2-k, k-1, -1):
                list.append(matrix[i][j])

            if len(list) == m*n: break
            j = k
            for i in range(m-2-k, k, -1):
                list.append(matrix[i][j])

        return list

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1], [2], [3], [4], [5]]
    solution = Solution()
    res = solution.spiralOrder(matrix)
    print res
