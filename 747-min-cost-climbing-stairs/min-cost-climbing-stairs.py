
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        hehe1 = hehe2 = 0
        for i in range(2, len(cost)):
            temp = hehe2
            hehe2 = min(hehe1 + cost[i - 2], hehe2 + cost[i-1])
            hehe1 = temp
        return min(hehe2 + cost[-1], hehe1 + cost[-2])
            