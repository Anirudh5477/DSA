import heapq
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.l = []
        for i in range(len(nums)):
            heapq.heappush(self.l, nums[i])
            if len(self.l) > k:
                heapq.heappop(self.l)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.l, val)
        if len(self.l) > self.k: 
            heapq.heappop(self.l)
        return self.l[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)