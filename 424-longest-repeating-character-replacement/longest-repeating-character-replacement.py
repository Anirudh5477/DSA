class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        left = 0
        dict_ = {}
        for i in range(len(s)):
            x = s[i]
            if x in dict_:
                dict_[x] += 1       
            else:
                dict_[x] = 1
            sorted_dict = sorted(dict_.items(), key = lambda x: x[1])
            sum_k = 0
            for j in range(len(dict_)-1):
                sum_k += sorted_dict[j][1]
            if sum_k>k:
                left += 1
                dict_[s[left-1]] -=1
            if i-left+1 > ans:
                ans = i-left + 1
        return ans


                
            
            

        