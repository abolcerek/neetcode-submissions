class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        # decision tree
        # we either add nothing or add the next value
        # Input: nums = [1,2,1]
        #                1  12 
        #                       121
        #
        #
        #
        #
        #
        #
        #
        #


        def dfs(i):
            if i >= len(nums):
                if subset.copy() not in res:
                    res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res