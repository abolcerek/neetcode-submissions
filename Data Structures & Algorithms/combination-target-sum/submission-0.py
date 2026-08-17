class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
 
        res = []

        def dfs(i, cur, score):
            if score == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or score > target:
                return
            
            cur.append(nums[i])
            dfs(i, cur, score + nums[i])
            cur.pop()
            dfs(i+1, cur, score)

        dfs(0, [], 0)
        return res 