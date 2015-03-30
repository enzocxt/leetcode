class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0: return False

        div = 1
        while x/div >= 10:
            div *= 10

        while x:
            left = x / div
            right = x % 10

            if left != right:
                return False

            x = (x%div) / 10
            div = div/100

        return True

if __name__ == '__main__':
    x = 134431
    solution = Solution()
    res = solution.isPalindrome(x)
