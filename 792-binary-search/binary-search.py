class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        if not(nums[left]<=target<=nums[right]):
            return -1
        while right>=left:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif target>nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


        