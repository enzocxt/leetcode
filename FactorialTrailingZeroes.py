class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        x = 5
        res = 0
        while n >= x:
            res += n / x
            x *= 5

        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.trailingZeroes(28)
    print res
