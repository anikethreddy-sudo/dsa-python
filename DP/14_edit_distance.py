def min_distance(word1, word2):
    rows = len(word1)
    cols = len(word2)

    dp = [[0] * (cols + 1) for _ in range(rows + 1)]

    for i in range(rows + 1):
        dp[i][cols] = rows - i

    for j in range(cols + 1):
        dp[rows][j] = cols - j

    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i + 1][j],      # Delete
                    dp[i][j + 1],      # Insert
                    dp[i + 1][j + 1]   # Replace
                )

    return dp[0][0]


word1 = "horse"
word2 = "ros"

print(min_distance(word1, word2))
