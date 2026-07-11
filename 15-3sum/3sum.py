class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j<k:
                _sum = nums[j] + nums[k]
                if _sum<-nums[i]:
                    j+=1
                elif _sum>-nums[i]:
                    k-=1
                else :
                    maybe = [nums[i],nums[j],nums[k]]    
                    ans.append(maybe)
                    while j<k and nums[j] == nums[j+1]:
                        j+=1
                    while j<k and nums[k] == nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
        return ans
                    
                
        

        