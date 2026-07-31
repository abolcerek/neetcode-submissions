class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
        outer_l = 0
        outer_r = len(matrix) - 1
        while outer_l <= outer_r:
            mid = (outer_r - outer_l) + outer_l // 2
            min_val = min(matrix[mid])
            max_val = max(matrix[mid])
            if min_val <= target <= max_val:
                l = 0
                r = len(matrix[mid]) - 1
                while l <= r:
                    inner_mid = (r - l) + l // 2
                    if matrix[mid][inner_mid] == target:
                        return True
                    if matrix[mid][inner_mid] > target:
                        r = inner_mid - 1
                    if matrix[mid][inner_mid] < target:
                        l = inner_mid + 1
                return False
            if target > max_val:
                outer_l = mid + 1
            if target < min_val:
                outer_r = mid - 1
        return False 
