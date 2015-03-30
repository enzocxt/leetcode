class Solution:
    # @return a string
    def titleToNumber(self, s):
        res = 0
        #s = s[::-1]
        #for i in range(len(s)):
        #    res += (ord(s[i])-ord('A') + 1) * 26**i
        for e in s:
            res = res * 26 + ord(e) - ord('A') + 1

        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.titleToNumber('AR')
    print res
