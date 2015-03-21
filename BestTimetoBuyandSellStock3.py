class Solution:
    # @param prices, a list of integer
    # @return a integer
    def maxProfit(self, prices):
        size = len(prices)
        if size <= 1: return 0
        f1 = [0 for i in range(size)]
        f2 = [0 for i in range(size)]

        minV = prices[0]
        for i in range(1, size):
            minV = min(minV, prices[i])
            f1[i] = max(f1[i-1], prices[i]-minV)

        maxV = prices[size-1]
        for i in range(size-2, -1, -1):
            maxV = max(maxV, prices[i])
            f2[i] = max(f2[i+1], maxV-prices[i])

        res = 0
        for i in range(size):
            if f1[i]+f2[i] > res:
                res = f1[i] + f2[i]

        return res

if __name__ == '__main__':
    prices = [2, 3, 5, 1, 6, 3]
    prices = [3, 1, 2, 4, 5, 2, 6]
    prices = [1, 4, 2]
    solution = Solution()
    res = solution.maxProfit(prices)
    print res
