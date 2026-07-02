class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = 0
        for i in nums:
            if i!=0:
                total *= i
            else:
                zero_count += 1
        if zero_count == 0:
            answer = [total//i for i in nums]
        elif zero_count == 1:
            answer = [0 if i!= 0 else total for i in nums]
        else:
            answer = [0]*len(nums)
        return answer