class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        for i in xrange(len(num)):
            x = num[i]
            if target-x in dict:
                return (dict[target-x]+1, i+1)
            dict[x] = i

if __name__ == '__main__':
    solution = Solution()
    num = [3, 2, 4]
    res = solution.twoSum(num, 6)
    print res
