class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowered = s.lower()
        l = 0
        r = len(s) - 1
        while l <= r:
            if lowered[l].isalnum() == False:
                l += 1
                continue
            if lowered[r].isalnum() == False:
                r -= 1
                continue
            if lowered[l] != lowered[r]:
                return False
            else:
                l += 1
                r -= 1
        return True