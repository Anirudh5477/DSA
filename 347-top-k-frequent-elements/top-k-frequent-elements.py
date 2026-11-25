from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        ans = []
        ans_freq = []
        for num, freq in counts.items() : 
            if len(ans) < k:
                ans.append(num)
                ans_freq.append(freq)
            else:
                minim = 0
                for i in range(len(ans_freq)):
                    if ans_freq[i] < ans_freq[minim]:
                        minim = i
                if freq > ans_freq[minim]:
                    ans[minim] = num
                    ans_freq[minim] = freq
        return ans
                    

        