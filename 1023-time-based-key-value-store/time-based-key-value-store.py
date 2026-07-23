class TimeMap:

    def __init__(self):
        self.ds = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.ds:
            self.ds[key].append((value,timestamp))
        else:
            self.ds[key] = [(value,timestamp)]
        
        
    
    def get(self, key: str, timestamp: int) -> str:
        # Key doesn't exist yet
        if key not in self.ds:
            return ""
        
        l = self.ds[key]
        left = 0
        right = len(l) - 1
        ans = ""
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if l[mid][1] <= timestamp:
                ans = l[mid][0]   # Store current best answer
                left = mid + 1    # Keep searching to the right for a larger timestamp
            else:
                right = mid - 1   # Target is smaller, search to the left
                
        return ans

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)