from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1
        letters = Counter(s1)
        count = Counter(s2[left : right])
        while right < len(s2):
            if s2[right] in count:
                count[s2[right]] += 1
            else:
                count[s2[right]] = 1
            if count == letters:
                return True
            count[s2[left]] -= 1
            if count[s2[left]] == 0:
                del count[s2[left]]
            left+=1
            right+=1
        return False
        