class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @ return a list of lists of integers
    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            return Solution.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target-candidates[i], i, valuelist+[candidates[i]])

    def combinationSum(self, candidates, target):
        if len(candidates) == 0: return 0
        candidates.sort()
        Solution.ret = []
        self.DFS(candidates, target, 0, [])
        return Solution.ret

if __name__ == '__main__':
    A = [2, 3, 6, 7]
    solution = Solution()
    res = solution.combinationSum(A, 7)
    print res
