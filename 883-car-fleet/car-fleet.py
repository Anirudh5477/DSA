class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed))
        times = [(target-p)/s for p,s in cars]
        ans=0
        while len(times)>1:
            curr = times.pop()
            if curr<times[-1]:
                ans+=1
            else:
                times[-1] = curr
        return ans + 1


        