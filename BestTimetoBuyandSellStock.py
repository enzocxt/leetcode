class Solution:
    # @param prices, a list of integer
    # @return a integer
    def maxProfit(self, prices):
        size = len(prices)
        if size <= 1: return 0

        low = prices[0]
        maxprofit = 0
        for i in prices:
            if i < low:
                low = i
            maxprofit = maxprofit if maxprofit > i-low else i-low

        return maxprofit

if __name__ == '__main__':
    prices = [2, 1]
    solution = Solution()
    res = solution.maxProfit(prices)
    print res
