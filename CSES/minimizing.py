n,x=map(int,input().split())
coins=sorted(map(int,input().split()))
INF=float('inf')
dp=[INF]*(x+1)
dp[0]=0
for i in range(1,x+1):
    for coin in coins:
        if coin>i:
            break
        dp[i]=min(dp[i],dp[i-coin]+1)
if dp[x]==INF:
    print(-1)
else:
    print(dp[x])