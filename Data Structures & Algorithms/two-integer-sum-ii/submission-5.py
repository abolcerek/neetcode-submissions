class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        while l < r:
            if r == len(numbers):
                l += 1
                r = l + 1
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            else:
                r += 1
        