def max_subarray(nums):
    current = nums[0]
    maximum = nums[0]

    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        maximum = max(maximum, current)

    return maximum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(nums)) 
