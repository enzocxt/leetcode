class Solution:
    # @return an integer
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        res = 0

        while left < right:
            water = min(height[left], height[right]) * (right - left)
            if water > res: res = water
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res

    def maxArea_n2(self, height):
        n = len(height)
        if n <= 1: return 0

        valuelist = [0 for i in range(n)]
        for i in range(1, n+1):
            j = i+1
            while j < n+1:
                valuelist[i-1] = max(valuelist[i-1], min(height[i-1], height[j-1]) * (j-i))
                j += 1

        res = 0
        for k in range(n):
            res = max(res, valuelist[k])

        return res

if __name__ == '__main__':
    height = [3, 1, 2, 5, 4]
    solution = Solution()
    res = solution.maxArea(height)
    print res
