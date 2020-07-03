def decompressRLElist(nums):
    output = []
    for i in range(0, len(nums)-1, 2):
        temp = [nums[i + 1]] * (nums[i])
        output += temp

    return output

nums = [1,2,3,4]
print (decompressRLElist(nums))