class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # need to return base times height
        # base is the difference between the end and start index
        # height is the minimum container value

        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            base = r - l
            height = min(heights[l], heights[r])
            area = base * height
            max_area = max(area, max_area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_area


        # [1,7,2,5,4,7,3,6]