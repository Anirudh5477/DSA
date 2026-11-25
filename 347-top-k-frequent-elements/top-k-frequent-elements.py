from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        ans = []
        ans_freq = []
        for num, freq in counts.items() : 
            if len(ans) < k:
                j = len(ans)
                if j == 0:
                    ans.append(num)
                    ans_freq.append(freq)
                    continue
                while freq > ans_freq[j-1]:
                    j-=1
                    if j == 0:
                        break 
                ans.insert(j, num)
                ans_freq.insert(j, freq)
            else:
                j = len(ans)
                while freq > ans_freq[j-1]:
                    j-=1
                    if j == 0:
                        break
                ans.insert(j,num)
                ans_freq.insert(j,freq)
                ans.pop()
                ans_freq.pop()
        return ans
                    

        