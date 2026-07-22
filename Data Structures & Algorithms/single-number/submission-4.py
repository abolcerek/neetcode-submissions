class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visit = set()
        for i in nums:
            if i in visit:
                visit.remove(i)
            else:
                visit.add(i)
        return list(visit)[0]