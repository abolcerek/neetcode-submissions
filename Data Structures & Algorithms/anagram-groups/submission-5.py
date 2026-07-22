class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loops through strs and store the original with the sorted
        hashmap = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in hashmap:
                hashmap[sorted_word].append(word)
            else:
                hashmap[sorted_word] = [word]
        res = []
        for key, value in hashmap.items():
            res.append(value)
        return res