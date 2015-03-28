class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        res = ''
        if numerator == 0:
            return str(numerator)
        if (numerator<0) ^ (denominator<0):
            res += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        units = numerator / denominator
        res += str(units)
        if numerator%denominator == 0: return res
        res += '.'
        remainder = numerator % denominator
        dict = {}

        while remainder:
            if remainder in dict:
                res = res[:dict[remainder]] + '(' + res[dict[remainder]:] + ')'
                break
            dict[remainder] = len(res)
            remainder *= 10
            res += str(remainder / denominator)
            remainder %= denominator

        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.fractionToDecimal(2, 1)
    print res
