import sys

MOD = 1000000007
n, x = map(int, sys.stdin.readline().split())
coins = list(map(int, sys.stdin.readline().split()))
dp = [0] * (x + 1)
dp[0] = 1
for i in range(1, x + 1):
    curr = 0
    for coin in coins:
        if coin <= i:
            curr += dp[i - coin]
    dp[i] = curr % MOD
print(dp[x])