class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        pascal = []
        pascal.append([1])

        i = 0
        # i = 0, 1, ... , numRows-1
        while i < numRows-1:
            row = []
            row.append(1)
            j = 0
            while j < i:
                row.append(pascal[i][j] + pascal[i][j+1])
                j = j+1
            row.append(1)
            print row
            pascal.append(row)
            i = i+1

        return pascal

    def getRow(self, rowIndex):
        line = []
        line.append(1)
        if rowIndex == 0:
            return line

        if rowIndex == 1:
            line.append(1)
            return line

        i = 2
        while i <= rowIndex:
            j = i - 1
            line.append(1)
            while j > 0:
                line[j] = line[j] + line[j-1]
                j = j-1
            i = i + 1

        line.append(1)

        return line

if __name__ == '__main__':
    numRows = 4
    solution = Solution()
    res = solution.generate(numRows)
    res = solution.getRow(numRows)
    print res
