
def rotate(nums, k):
    if k < len(nums):
        length = len(nums)
        m = length - k
        nums_part = nums[:m]
    
        for i in range(k):
            nums[i] = nums[m+i]

        nums[k:] = nums_part
    else:
        rotate(nums, k-len(nums))

    return nums

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7]
    print rotate(array, 11)
