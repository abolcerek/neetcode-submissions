class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        sorted_hash = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse = True))
        count = k
        for key, value in sorted_hash.items():
            if count == 0:
                return res
            else:
                res.append(key)
                count -= 1
        return res

        


