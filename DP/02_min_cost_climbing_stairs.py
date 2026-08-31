def min_cost_climbing_stairs(cost):
    first = cost[0]
    second = cost[1]

    for i in range(2, len(cost)):
        current = cost[i] + min(first, second)
        first = second
        second = current

    return min(first, second)


cost = [10, 15, 20]
print(min_cost_climbing_stairs(cost))
