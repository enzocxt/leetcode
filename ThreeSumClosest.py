class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        mindiff = 100000
        res = 0

        for i in range(len(num)):
            left = i+1
            right = len(num)-1

            while left < right:
                sum = num[i] + num[left] + num[right]
                diff = abs(sum-target)
                if diff < mindiff:
                    mindiff = diff
                    res = sum
                if sum == target:
                    return sum
                elif sum < target:
                    left += 1
                else: right -= 1

        return res

    def threeSumClosest_bad(self, num, target):
        if num == []:
            return 0
        res1 = -1
        res2 = -1
        sum1 = sum2 = target

        while 1:
            for i in range(len(num)):
                dict = {}
                temp = num[i+1:]
                target2 = sum1 - num[i]

                for j in range(len(temp)):
                    x = temp[j]
                    if target2-x in dict:
                        res1 = sum1-target
                        break
                    dict[x] = j

                if res1 != -1:
                    break

            if res1 == -1:
                sum1 = sum1 + 1
            else:
                break


            for i in range(len(num)):
                dict = {}
                temp = num[i+1:]
                target2 = sum2 - num[i]

                for j in range(len(temp)):
                    x = temp[j]
                    if target2-x in dict:
                        res2 = target-sum2
                        break
                    dict[x] = j

                if res2 != -1:
                    break

            if res2 == -1:
                sum2 = sum2 - 1
            else:
                break

        if res1 < res2:
            return target + res1
        else:
            return target - res2

if __name__ == '__main__':
    S = [-1, 2, 1, -4]
    #S = [0, 0, 0]
    solution = Solution()
    res = solution.threeSumClosest(S, 1)
    print res
