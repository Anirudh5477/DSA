class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i == 0:
                prev = nums[i]
                i+=1
                continue
            elif prev == nums[i]:
                del nums[i]

            else:
                prev = nums[i]
                i+=1
        return len(nums)
        