class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        candidate, count = None, 0

        for e in num:
            if count == 0:
                candidate, count = e, 1
            elif e == candidate:
                count += 1
            else:
                count -= 1

        return candidate

if __name__ == '__main__':
    num = [1, 2, 3, 3, 3, 2, 2, 2, 5, 4, 2, 2]
    solution = Solution()
    res = solution.majorityElement(num)
    print res
