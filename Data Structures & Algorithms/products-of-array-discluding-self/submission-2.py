from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Input: nums = [-1,0,1,2,3]

        res = []
        for i, num in enumerate(nums):
            before = nums[:i]
            after = nums[i + 1:]
            if len(before) == 0:
                res.append(prod(after))
                continue
            if len(after) == 0:
                res.append(prod(before))
                continue
            else:
                result = prod(before) * prod(after)
                res.append(result)
        return res
            