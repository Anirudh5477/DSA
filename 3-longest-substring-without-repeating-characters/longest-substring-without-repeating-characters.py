class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = -1
        right = 0
        pos = dict()
        ans = 0
        while right<len(s):
            if s[right] in pos:
                if left < pos[s[right]]:
                    left = pos[s[right]] 
                    pos[s[right]] = right
                else:
                    pos[s[right]] = right
            else:
                pos[s[right]] = right

            if right - left > ans:
                ans = right - left
            right += 1
        return ans 



        