class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)-1):
            add = prices[i+1] - prices[i]
            ans+= add if add>0 else 0
        return ans

        