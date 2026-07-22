class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap1 = {}
        hashmap2 = {}

        for c in s:
            if c not in hashmap1:
                hashmap1[c] = 1
            else:
                hashmap1[c] += 1
        

        for c in t:
            if c not in hashmap2:
                hashmap2[c] = 1
            else:
                hashmap2[c] += 1

        if hashmap1 == hashmap2:
            return True
        return False