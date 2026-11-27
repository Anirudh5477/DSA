class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        sorted_pos = sorted(zip(position, speed))
        l = []
        n = len(position)
        for i in range(n):
            pos, s = sorted_pos[n - i -1]
            t = (target - pos)/s
            if not l:
                l.append(t)
            t_prev = l[-1]
            if t > t_prev : 
                l.append(t)
        return len(l)
