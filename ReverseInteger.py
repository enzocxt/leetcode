#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @return an integer
    def reverse(self, x):
        newN = 0
        left = 0
        while x != 0:
            left = x%10
            if x<0 and x>-10:
                left = x
            newN = newN*10 + left
            x = x/10
        
        if abs(newN) >= 2**31-1:
            newN = 0

        return newN

    def reverse_version2(self, x):
        lastDigit = 0
        result = 0

        if x<0:
            flag = -1
        else:
            flag = 1
        x = abs(x)
        
        while x>0:
            lastDigit = x%10
            result = result*10 + lastDigit
            x = x/10

        if result < 0:
            return 0
        
        if result >= 2**31-1:
            result = 0

        return result*flag

    def reverse_l(self, x):
        x_list = []
        if x < 0:
            flag = -1
        else:
            flag = 1

        x = abs(x)
        while x >= 10:
            temp = x%10
            x_list.append(temp)
            x = x/10
        x_list.append(x)

        i = 0
        while len(x_list) and x_list[i] == 0:
            x_list.remove(x_list[i])

        print x_list
        x = 0
        for i in range(len(x_list)):
            x = x + x_list[i]*10**(len(x_list)-i-1)

        if x >= 2**31-1:
            x = 0

        return x * flag

solution = Solution()
print solution.reverse(0)
print solution.reverse(10)
print solution.reverse(-100)
print solution.reverse(1231241242)
