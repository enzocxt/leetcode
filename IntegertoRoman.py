class Solution:
    # @return a string
    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        list = ''
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                list += numerals[i]

        return list
