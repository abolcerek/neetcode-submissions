class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {sorted word: [unsorted_word_1, unsorted_word_2]}
        # strs = ["act","pots","tops","cat","stop","hat"]
        # strs = ['act', opst, ]
        original = strs #
        hashmap = {}
        res = []
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            if sorted_word in hashmap.keys():
                hashmap[sorted_word].append(original[i])
            else:
                hashmap[sorted_word] = [original[i]]
        for key, values in hashmap.items():
            res.append(values)
        return res

        
            
