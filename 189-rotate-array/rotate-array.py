class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if len(nums)== 1:
            return 
        nums.reverse()
        nums[0:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        
        