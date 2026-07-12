class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_v = 0
        while left<right:
            num1 = height[left]
            num2 = height[right]
            if num2>num1:
                v = (right-left) * min(num2,num1)
                max_v = max(max_v,v)
                left += 1
            else:
                v = (right-left) * min(num1,num2)
                max_v = max(max_v,v)
                right -= 1
        return max_v


        