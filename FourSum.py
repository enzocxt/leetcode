class Solution:
    # @return a list of lists of length 4, [[val1, val2, val3, val4]]
    def fourSum(self, num, target):
        numLen = len(num)
        res = set()
        dict = {}
        if numLen < 4:
            return []
        num.sort()

        for i in range(numLen):
            for j in range(i+1, numLen):
                if num[i]+num[j] not in dict:
                    dict[num[i]+num[j]] = [(i, j)]
                else:
                    dict[num[i]+num[j]].append((i, j))

        for i in range(numLen):
            for j in range(i+1, numLen-2):
                T = target - num[i] - num[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j:
                            res.add((num[i], num[j], num[k[0]], num[k[1]]))

        return [list(i) for i in res]

    def fourSum2(self, num, target):
        numLen = len(num)
        res = set()
        dict = {}
        if numLen < 4:
            return []
        num.sort()

        for i in range(numLen):
            for j in range(i+1, numLen):
                if num[i]+num[j] not in dict:
                    dict[num[i]+num[j]] = [(i, j)]
                else:
                    dict[num[i]+num[j]].append((i, j))

        num2 = []
        for i in dict:
            num2.append(i)
        num2.sort()

        for i in range(len(num2)):
            x = num2[i]
            if target-x in dict:
                for k in dict[target-x]:
                    for l in dict[x]:
                        line = []
                        line.append(num[k[0]])
                        line.append(num[k[1]])
                        line.append(num[l[0]])
                        line.append(num[l[1]])
                        line.sort()
                        res.add((line[0], line[1], line[2], line[3]))

        return [list(i) for i in res]

if __name__ == '__main__':
    #num = [1, 0, -1, 0, -2, 2]
    num = [2, 1, 0, -1]
    solution = Solution()
    #res = solution.fourSum2(num, 0)
    res = solution.fourSum(num, 2)
    print res
