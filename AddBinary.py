class Solution:
    # @param, a, a string
    # @param, b, a string
    # @return a string
    def addBinary(self, a, b):
        a = a[::-1]; b = b[::-1]
        c = [0 for i in range(max(len(a), len(b)) + 1)]
        for i in range(min(len(a), len(b))):
            c[i] = int(a[i]) + int(b[i])
        if len(a) < len(b):
            for i in range(len(a), len(b)):
                c[i] = int(b[i])
        else:
            for i in range(len(b), len(a)):
                c[i] = int(a[i])
        for i in range(len(c)-1):
            c[i+1] += c[i] / 2
            c[i] = c[i] %2
        i = len(c)-1
        while c[i] == 0:
            c.pop()
            i -= 1
        c = c[::-1]
        res = ''.join(str(e) for e in c)
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.addBinary("111", "1010")
    print res
