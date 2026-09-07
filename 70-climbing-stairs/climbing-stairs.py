class Solution:
    def climbStairs(self, n: int) -> int:
        f1 = 1
        f2 = 2
        if n == 1:
            return 1

        for i in range(n-2):
            f1 , f2 = f2, f1 + f2
        return f2
