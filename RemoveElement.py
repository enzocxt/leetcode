class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i, j = 0, 0
        for i in range(len(A)):
            if A[i] == elem:
                continue

            A[j] = A[i]
            j = j + 1

        return j

if __name__ == '__main__':
    A = [1, 2, 2, 3, 2, 4]
    solution = Solution()
    print solution.removeElement(A, 2)
