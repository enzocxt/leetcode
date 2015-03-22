class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if len(num) <= 1: return num
        partition = -1
        for i in range(len(num)-2, -1, -1):
            if num[i] < num[i+1]:
                partition = i
                break

        if partition == -1:
            num.reverse()
            return num
        else:
            for i in range(len(num)-1, partition, -1):
                if num[i] > num[partition]:
                    num[i], num[partition] = num[partition], num[i]
                    break

        left = partition+1
        right = len(num)-1
        while left < right:
            num[left], num[right] = num[right], num[left]
            left += 1
            right -= 1

        return num
