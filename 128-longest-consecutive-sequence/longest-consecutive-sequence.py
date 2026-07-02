class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seen = set()
        max = 0
        for i in nums:
            if i not in seen:
            
                if i-1 not in nums:
                    count = 1
                    while i + count in nums:
                        count+=1
                    if count > max:
                        max = count
            else:
                continue   
        return max     
                
        