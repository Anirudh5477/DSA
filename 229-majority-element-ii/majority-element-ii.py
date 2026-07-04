class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums)
        len3 = length//3
        if length == 1:
            return nums
        count1 = 0
        count2 = 0
        candidate1 = None
        candidate2 = None

        for i in nums:
            if i == candidate1:
                count1 +=1
            elif i == candidate2:
                count2+=1
            elif count1==0:
                candidate1 = i
                count1+=1
            elif count2 == 0:
                candidate2 = i
                count2+=1
            else:
                count1 -=1
                count2-=1
        if candidate1!=None and candidate2 !=None and nums.count(candidate1)>len3 and nums.count(candidate2)>len3:
            return [candidate1,candidate2]
        elif candidate1!=None and nums.count(candidate1) >len3 :
            return [candidate1]
        elif nums.count(candidate2)>len3:
            return[candidate2]
        else:
            return []
        


        