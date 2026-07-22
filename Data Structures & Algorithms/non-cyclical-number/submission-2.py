class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumofsquares(n)
            if n == 1:
                return True
        return False
        


    def sumofsquares(self, n: int) -> bool:
        output = 0

        while n:
            digits = n % 10
            digits = digits ** 2
            output += digits
            n = n // 10
        return output