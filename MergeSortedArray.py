class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing(void)
    def merge(self, A, m, B, n):
        i, j, k = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
            k -= 1

        while j >= 0:
            A[k] = B[j]
            j -= 1
            k -= 1

if __name__ == '__main__':
    global A, B
    A = [0, 0]
    B = [1]
    #A = [1, 2, 5, 7]
    #B = [2, 3, 4, 8]
    solution = Solution()
    solution.merge(A, len(A), B, len(B))
    print A
