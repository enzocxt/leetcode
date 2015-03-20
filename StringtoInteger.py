#!/usr/bin/env python

class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()

        if str == '':
            return 0

        INT_MAX, INT_MIN = 2**31-1, -1*2**31
        flag = 1

        # str = '+1'
        if str[0] in '+-':
            if str[0] == '-':
                flag = -1
            str = str[1:]

        if str.isdigit():
            result = int(str)
        else:
            i = 0
            while str[i].isdigit():
                i += 1
            if i != 0:
                str = str[:i]
                result = int(str)
            else:
                return 0

        # str = '12345678987654321'
        if result > INT_MAX:
            return INT_MIN if flag == -1 else INT_MAX

        return result*flag

if __name__ == '__main__':
    solution = Solution()
    print solution.atoi('1')
    print solution.atoi('+-1')
    print solution.atoi('+-2')
    print solution.atoi('abc')
    print solution.atoi(' -12412jsdfi')
    print solution.atoi('132311231231')
