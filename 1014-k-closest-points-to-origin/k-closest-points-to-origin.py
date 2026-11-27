import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        points = [[x**2 + y**2,x,y] for x,y in points]
        heapq.heapify(points)
        ans = []
        for i in range(k):
            _,x,y= heapq.heappop(points)
            ans.append([x,y])
        return ans
        