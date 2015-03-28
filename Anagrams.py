class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        dict = {}

        for word in strs:
            sortedword = ''.join(sorted(word))
            dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]

        res = []
        for item in dict:
            if len(dict[item]) > 1:
                res += dict[item]

        return res

if __name__ == '__main__':
    strs = ["abc", "bac", "bca", "acb", "bbb"]
    solution = Solution()
    res = solution.anagrams(strs)
    print res
