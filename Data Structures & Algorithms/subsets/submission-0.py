class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())#add the subsset into the res
                return res

            #decision to include nums[i]
            #left side of the backtracking
            subset.append(nums[i])
            dfs(i + 1)

            #decision NOT to include nums[i]

            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
