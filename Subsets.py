class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        solutions = []
        S.sort()
        bits = len(S)

        for i in range(1 << bits):
            solution = []
            for j in range(bits):
                if i & (1 << j):
                    solution.append(S[j])
            solutions.append(solution)

        return solutions

    def subsets_dp(self, S):
        def dfs(depth, start, valuelist):
            ret.append(valuelist)
            if depth == len(S): return
            for i in range(start, len(S)):
                dfs(depth+1, i+1, valuelist+[S[i]])

        S.sort()
        S.reverse()
        ret = []
        dfs(0, 0, [])

        return ret

if __name__ == '__main__':
    S = [1, 2, 3]
    solution = Solution()
    res = solution.subsets(S)
    print res
