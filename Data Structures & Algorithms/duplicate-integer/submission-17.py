class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        rando = set()
        for i in nums:
            if i in rando:
                return True
            else:
                rando.add(i)
        return False