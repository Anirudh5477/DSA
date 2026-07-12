class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        prev = 0
        ans = 0
        while left<right:
            num1 = height[left]
            num2 = height[right]
            if num1>=num2:
                if num2<=prev:
                    ans-=num2
                    right-=1
                else:
                    ans+=(num2-prev)*(right-(left+1))
                    ans-=prev
                    prev = num2
                    right-=1
            else:
                if num1<=prev:
                    ans-=num1
                    left+=1
                else:
                    ans+=(num1-prev)*(right-(left+1))
                    ans-=prev
                    prev = num1
                    left+=1
        return ans
            


            
        