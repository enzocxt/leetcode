class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        i = 0
        j = len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target: return True
            elif matrix[i][j] > target: j -= 1
            else: i += 1

        return False

    def searchMatrix_bad(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m-1
        line = 0
        while l < r:
            mid = (l+r) / 2
            if matrix[l][0] > target:
                return False
            elif matrix[l][0] <= target and matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] <= target and matrix[r][0] > target:
                l = mid
            else:
                line = m-1
                break

        l = 0
        r = n-1
        while l <= r:
            mid = (l+r) / 2
            if matrix[line][mid] == target:
                return True
            elif matrix[line][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False

if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    matrix = [[1, 3, 5, 7]]
    solution = Solution()
    res = solution.searchMatrix(matrix, 3)
    print res
