class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # left and right pointers
        # area = base * height
        # base = right - left
        # height = min(left, right)
        # adjust left and right pointers based on who is less

        # height = [1,7,2,5,4,7,3,6]
                   #l             r

        #base = 
        res = 0

        left, right = 0, len(heights) - 1
        while left < right:
            base = right - left
            height = min(heights[left], heights[right])
            res = max(res, base * height)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res