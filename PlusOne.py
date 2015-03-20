class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        i = len(digits) - 1
        sum, one = 0, 1
        res = []

        while i >= 0:
            sum = digits[i] + one
            one = sum / 10
            res.append(sum % 10)
            i = i-1

        if one > 0:
            res.append(1)

        res.reverse()

        return res

    def plusOne2(self, digits):
        if digits == []:
            return 0

        digits.reverse()
        list = digits
        list.append(0)

        list[0] = list[0] + 1
        for i in range(len(list)):
            if list[i] == 10:
                list[i] = 0
                list[i+1] = list[i+1] + 1

        if list[-1] == 0:
            list = list[:-1]
        list.reverse()

        return list

if __name__ == '__main__':
    digits = [[0], [1], [9], [9,9], [1,9,9]]
    solution = Solution()
    for i in digits:
        res = solution.plusOne(i)
        print res
