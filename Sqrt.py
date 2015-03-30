class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x == 0 or x == 1: return x
        left = 1
        right = x-1
        while left <= right:
            mid = (left + right) / 2
            if mid * mid == x: return mid
            elif left*left <= x < mid*mid:
                right = mid - 1
            elif mid*mid < x <= right*right:
                left = mid + 1

        if mid * mid != x:
            return 0
        return mid

if __name__ == '__main__':
    solution = Solution()
    res = solution.sqrt(1225)
    print res
