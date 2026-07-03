class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        length = len(nums)
        len3 = length//3
        done = set()
        for i in nums:
            if i not in done:
                if i in count:
                    count[i] +=1
                    if count[i] >len3:
                        done.add(i)
                        del count[i]
                else:
                    count[i] = 1
                    if count[i] >len3:
                        done.add(i)
                        del count[i]
                        
        return list(done)


        