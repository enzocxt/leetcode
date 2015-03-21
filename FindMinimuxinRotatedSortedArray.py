class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        numLen = len(num)

        if numLen == 0:
            return 0
        elif numLen == 1:
            return num[0]
        #elif numLen == 2:
        #    return num[0] if num[0]<num[1] else num[1]

        start = 0
        stop = numLen - 1

        while start < stop-1:
            if num[start] < num[stop]:
                return num[start]

            mid = (start + stop) / 2
            if num[start] < num[mid]:
                start = mid
            else:
                stop = mid

        return num[start] if num[start]<num[stop] else num[stop]

if __name__ == '__main__':
    #num = [4, 5, 6, 7, 0, 1, 2]
    num = [1, 2]
    solution = Solution()
    res = solution.findMin(num)
    print res
