MOD=10**9+7
n=int(input())
dp=[-1]*(n+1)
def solve(x):
    if x==0:
        return 1
    if x<0:
        return 0
    if dp[x]!=-1:
        return dp[x]
    ans=0
    for i in range(1,7):
        ans=(ans+solve(x-i))%MOD
    dp[x]=ans
    return ans
print(solve(n))