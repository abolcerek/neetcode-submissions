class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        while l < r:
            diff = target - nums[l]
            if nums[r] == diff:
                return [l, r]
            r += 1
            if r == len(nums):
                l += 1
                r = l + 1 