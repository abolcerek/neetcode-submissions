class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        if len(s) != len(t):
            return False
        for i in s:
            hashmap1[i] = 1 + hashmap1.get(i, 0)
        for i in t:
            hashmap2[i] = 1 + hashmap2.get(i, 0)
        
        return hashmap1.items() == hashmap2.items()


        