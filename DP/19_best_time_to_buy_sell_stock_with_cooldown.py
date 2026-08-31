def max_profit(prices):
    if not prices:
        return 0

    buy = -prices[0]
    sell = 0
    cooldown = 0

    for price in prices[1:]:
        prev_buy = buy
        buy = max(buy, cooldown - price)
        cooldown = sell
        sell = max(sell, prev_buy + price)

    return sell


prices = [1, 2, 3, 0, 2]
print(max_profit(prices))
