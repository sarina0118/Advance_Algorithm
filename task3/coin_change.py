def coin_change_limited(coins, limits, target):

    INF = float("inf")

    dp = [INF] * (target + 1)
    dp[0] = 0

    for i in range(len(coins)):

        coin = coins[i]
        limit = limits[i]

        new_dp = dp[:]

        for amount in range(target + 1):

            if dp[amount] != INF:

                for count in range(1, limit + 1):

                    new_amount = amount + coin * count

                    if new_amount <= target:

                        new_dp[new_amount] = min(
                            new_dp[new_amount],
                            dp[amount] + count
                        )

        dp = new_dp

    if dp[target] == INF:
        return -1

    return dp[target]