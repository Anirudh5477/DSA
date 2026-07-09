class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(left,right,count):
            if left>=right:
                return True
            elif s[left] == s[right]:
                return check(left+1,right-1,count)
            else:
                if count == 0:
                    return False
                case1 = check(left+1,right,0)
                case2 = check(left,right-1,0)
                return case1 or case2
        return check(0,len(s)-1,1)
        
        