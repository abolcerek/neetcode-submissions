class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashmap1 = {}
        hashmap2 = {}

        for i in range(len(s)):
            hashmap1[s[i]] = 1 + hashmap1.get(s[i], 0)
            hashmap2[t[i]] = 1 + hashmap2.get(t[i], 0)
        return hashmap1 == hashmap2

        