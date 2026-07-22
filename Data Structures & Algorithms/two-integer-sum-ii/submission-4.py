class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers = [100,200,300,500]     target = 500
        #                 l    r
        # value = 400
        l, r = 0, 1
        while l < r:
            value = target - numbers[l]
            if numbers[r] == value:
                return [l + 1, r + 1]
            if r == (len(numbers) - 1):
                l += 1
                r = l + 1
            else:
                r += 1
        