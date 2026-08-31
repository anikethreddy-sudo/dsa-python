def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                dp[value] = min(dp[value], dp[value - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1


coins = [1, 2, 5]
amount = 11

print(coin_change(coins, amount))
