from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =deque()
        ans = [0]*len(temperatures)
        for i,val in enumerate(temperatures):
            
            while stack and (temperatures[stack[-1]] < val):
                index = stack.pop()
                ans[index] = i-index
            stack.append(i)
        return ans
                



        