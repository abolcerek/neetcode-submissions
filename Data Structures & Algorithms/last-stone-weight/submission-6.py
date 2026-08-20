class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        # stones sorted = [6, 4, 3, 2, 2]
        # [2, 3, 2, 2]
        # [3, 2, 2, 2]
        # [1, 2, 2]
        # [2, 2, 1]
        # [1]

        while len(stones) > 1:
            stones.sort(reverse=True)
            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
            else:
                diff = abs(stones[0] - stones[1])
                stones.pop(0)
                stones[0] = diff
        if len(stones) == 1:
            return stones[0]
        else:
            return 0