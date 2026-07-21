class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left<right:
            mid = left + (right-left)//2
            t = sum(((pile-1)//mid)+1 for pile in piles)
            if t <=h:
                right = mid
            else:
                left = mid+1
        return left


        