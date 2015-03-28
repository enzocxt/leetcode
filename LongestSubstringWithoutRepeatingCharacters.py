class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        maxLen = 0
        dict = {}
        start = 0

        for i in range(len(s)):
            dict[s[i]] = -1

        for i in range(len(s)):
            if dict[s[i]] != -1:
                while start <= dict[s[i]]:
                    dict[s[start]] = -1
                    start += 1

            maxLen = max(i-start+1, maxLen)
            dict[s[i]] = i

        return maxLen

if __name__ == '__main__':
    s = "abcabcbb"
    s = "bbbbbbbb"
    solution = Solution()
    res = solution.lengthOfLongestSubstring(s)
    print res
