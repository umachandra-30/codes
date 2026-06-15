class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=prices[0]
        profit=0
        for i in range(1,len(prices)):
            cost=prices[i]-minimum
            profit=max(profit,cost)
            minimum=min(minimum,prices[i])
        return profit
        