
def lisLength(nums):
    
    if not nums:
        return 0
    a = [1] * len(nums)

    
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                a[i] = max(a[i], a[j] + 1)

    return max(a)


nums = input("Enter the values: ")

arr = [int(x) for x in nums.split()]

res = lisLength(arr)
print("output:", res)
