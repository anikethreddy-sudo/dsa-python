def rob(nums):
    if len(nums) == 1:
        return nums[0]

    def helper(arr):
        rob1 = 0
        rob2 = 0

        for money in arr:
            temp = max(rob1 + money, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

    return max(helper(nums[:-1]), helper(nums[1:]))


nums = [2, 3, 2]
print(rob(nums))
