class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        num1 = num1[::-1]; num2 = num2[::-1]
        result = [0 for i in range(len(num1)+len(num2))]

        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i+j] += int(num1[i]) * int(num2[j])

        ans = []
        for i in range(len(result)):
            digit = result[i] % 10
            carry = result[i] / 10
            if i < len(result)-1:
                result[i+1] += carry
            ans.insert(0, str(digit))

        while ans[0] == '0' and len(ans) > 1:
            del ans[0]

        return ''.join(ans)

if __name__ == '__main__':
    solution = Solution()
    res = solution.multiply('98', '9')
    print res
