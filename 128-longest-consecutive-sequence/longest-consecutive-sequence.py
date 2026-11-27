class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        ans = 0
        for i in nums:
            if i - 1 in nums:
                continue
            count = 1
            while i + count in nums:
                count +=1
            if count > ans:
                ans = count
        return ans