class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = m-1
        second = n-1
        count = -1
        while first>=0 and second>=0:
            if nums1[first]>nums2[second]:
                nums1[count] = nums1[first]
                count-=1
                first-=1
            else:
                nums1[count] = nums2[second]
                count-=1
                second-=1
        while first>=0:
            nums1[count] = nums1[first]
            first-=1
            count-=1
        while second>=0:
            nums1[count] = nums2[second]
            second -=1
            count-=1


        