from collections import deque
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumsum = ans = 0
        cum_dict = {0:1}
        for i in nums:
            cumsum += i
            target = cumsum - k
            if target in cum_dict:
                ans += cum_dict[target]
                
            if cumsum in cum_dict:
                cum_dict[cumsum] += 1
            else:
                cum_dict[cumsum] = 1
                
        return ans
            
            
            
        
            


            
        