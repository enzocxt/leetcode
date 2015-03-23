class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if A == []: return

        p0 = 0
        p2 = len(A) - 1
        i = 0
        while i <= p2:
            if A[i] == 2:
                A[i], A[p2] = A[p2], A[i]
                p2 -= 1
            elif A[i] == 0:
                A[i], A[p0] = A[p0], A[i]
                p0 += 1
                i += 1
            else:
                i += 1

    def sortColors_2loop(self, A):
        index = [0, 0, 0]
        for i in range(len(A)):
            if A[i] == 0: index[0] += 1
            elif A[i] == 1: index[1] += 1
            else: index[2] += 1

        for i in range(len(A)):
            if i < index[0]: A[i] = 0
            elif i < index[0]+index[1]: A[i] = 1
            else: A[i] = 2

if __name__ == '__main__':
    global A
    A = [1, 0, 1, 0, 2, 2, 0, 0, 1, 1]
    solution = Solution()
    solution.sortColors(A)
    print A
