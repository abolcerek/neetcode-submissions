class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # [2, 3, 4, 4, 5, 10, 20]
        #                  i
        # curr = 6
        # streak = 4
        if not nums:
            return 0
        nums.sort()
        print(nums)
        curr, streak = nums[0], 0
        res = 0
        i = 0

        while i < len(nums):
            print(f'This is nums[i]: {nums[i]}')
            print(f'This is curr: {curr}')
            print(f'This is streak: {streak}')
            if nums[i] != curr:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        return res
