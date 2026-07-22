class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashset = set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                return nums[i]
            hashset.add(nums[i])