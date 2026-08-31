def can_partition(nums):
    total = sum(nums)

    if total % 2 != 0:
        return False

    target = total // 2
    possible = {0}

    for num in nums:
        next_possible = set(possible)

        for value in possible:
            if value + num == target:
                return True
            next_possible.add(value + num)

        possible = next_possible

    return target in possible


nums = [1, 5, 11, 5]
print(can_partition(nums))
