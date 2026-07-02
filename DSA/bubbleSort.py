



def bubbleSort(nums):
    n = len(nums)
    flag = False
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True

        if not flag:
            return "Already sorted"
    return nums


print(bubbleSort([8, 5, 7, 3, 2]))

