class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash1 = {}
        hash2 = {}
        for c in s1:
            if c not in hash1:
                hash1[c] = 1
            else:
                hash1[c] += 1


        l = 0
        for r in range(len(s2)):
            if s2[r] not in s1 or s2[l] not in s1:
                l += 1
                continue
            distance = r - l + 1
            if distance == len(s1):
                window = s2[l:r+1]
                for c in window:
                    if c not in hash2:
                        hash2[c] = 1
                    else:
                        hash2[c] += 1
                if hash1 == hash2:
                    return True
                else:
                    l += 1
                    hash2 = {}
        return False
            
