class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashset1 = {}
        hashset2 = {}

        for i in range(len(s)):
            hashset1[s[i]] = 1 + hashset1.get(s[i], 0)
            hashset2[t[i]] = 1 + hashset2.get(t[i], 0)
        return hashset1 == hashset2

        