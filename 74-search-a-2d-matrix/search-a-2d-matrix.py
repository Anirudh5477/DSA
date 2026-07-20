class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = len(matrix)*len(matrix[0])
        if target<matrix[0][0] or target>matrix[len(matrix)-1][len(matrix[0])-1]:
            return False
        while left<=right:
            mid = left + (right-left)//2
            if matrix[mid//cols][mid%cols] == target:
                return True
            elif matrix[mid//cols][mid%cols] > target:
                right = mid-1
            else:
                left = mid + 1
        return False
        