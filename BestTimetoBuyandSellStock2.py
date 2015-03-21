class Solution:
    # @param prices, a list of integer
    # @return a integer
    def maxProfit(self, prices):
        if len(prices) <= 1: return 0

        maxprofit = 0
        for i in range(0, len(prices)-1):
            if prices[i] < prices[i+1]:
                maxprofit += prices[i+1] - prices[i]


        return maxprofit

if __name__ == '__main__':
    prices = [2, 3, 5, 1, 6, 3]
    solution = Solution()
    res = solution.maxProfit(prices)
    print res
