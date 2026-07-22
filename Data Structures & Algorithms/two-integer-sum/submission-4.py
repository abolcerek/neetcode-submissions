class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            value = target - n
            if value in hashmap:
                return [hashmap[value], i]
            hashmap[n] = i

        