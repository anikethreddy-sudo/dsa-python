def rob(nums):
    rob1 = 0
    rob2 = 0

    for money in nums:
        temp = max(rob1 + money, rob2)
        rob1 = rob2
        rob2 = temp

    return rob2


nums = [2, 7, 9, 3, 1]
print(rob(nums))
