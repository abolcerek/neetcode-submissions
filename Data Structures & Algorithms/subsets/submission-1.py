class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [] #defining array will with contain subsets

        subset = [] #subset used for backtracking

        def dfs(i): #we take in our input as the index 
            if i >= len(nums): #if the index value is greater or equal to the length of nums
                res.append(subset.copy()) #we append the subset into the res array
                return res #we return the array    
            subset.append(nums[i]) #left side of the backtracking ([1,2,3])
            dfs(i + 1)
            subset.pop() #right side of the backtracking ([0])
            dfs(i + 1)
        dfs(0) #running dfs at index 0
        return res #returning the result