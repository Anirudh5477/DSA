import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        if not stones:
            return 0
        heapq.heapify_max(stones)
        while len(stones) > 1:
            n1 = heapq.heappop_max(stones)
            n2 = heapq.heappop_max(stones)
            heapq.heappush_max(stones, abs(n2-n1))
        if len(stones) == 1:
            return heapq.heappop(stones)
        else:
            n1 = heapq.heappop(stones)
            n2 = heapq.heappop(stones)
            return n2 - n1
