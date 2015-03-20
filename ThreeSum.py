class Solution:
    # @return a list of lists of length 3, [[val1, val2, val3]]
    def threeSum(self, num):
        res = []
        num.sort()

        for i in range(len(num)):
            line = []
            dict = {}
            temp = num[i+1:]
            line.append(num[i])
            target = num[i] * (-1)

            for j in xrange(len(temp)):
                x = temp[j]
                if target-x in dict:
                    line.append(target-x)
                    line.append(x)
                    line.sort()
                    if line in res:
                        line = [num[i]]
                        continue
                    else:
                        res.append(line)
                        line = [num[i]]
                dict[x] = j

        return res

if __name__ == '__main__':
    A = [-1, 0, 1, 2, -1, -4]
    res = []
    solution = Solution()
    res = solution.threeSum(A)
    print res
