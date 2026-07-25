class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_ = float('inf')
        for i in prices:
            if i < min_:
                min_ = i
            if ans<(i - min_):
                ans =i- min_
        return ans

        