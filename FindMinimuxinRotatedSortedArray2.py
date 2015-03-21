class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        numLen = len(num)

        if numLen == 0:
            return 0

        L = 0
        R = numLen - 1

        while L < R and num[L] >= num[R]:
            M = (L + R) / 2
            if num[L] < num[M]:
                L = M + 1
            elif num[M] < num[R]:
                R = M
            else:#num[start] >= num[mid] and num[mid] >= num[stop]
                L += 1

        return num[L]

if __name__ == '__main__':
    #num = [4, 5, 6, 7, 0, 1, 2]
    num = [3, 3, 1]
    solution = Solution()
    res = solution.findMin(num)
    print res
