class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        left = 0
        dict_ = {}
        max_freq = s[0]
        for i in range(len(s)):
            x = s[i]
            if x in dict_:
                dict_[x] += 1  
                                     
            else:
                dict_[x] = 1
            if dict_[x]>dict_[max_freq]:
                    max_freq = x


            if i-left+1 - dict_[max_freq]>k:
                left += 1
                dict_[s[left-1]] -=1
            if i-left+1 > ans:
                ans = i-left + 1
        return ans


                
            
            

        