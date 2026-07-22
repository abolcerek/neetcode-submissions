class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # ["act","pots","tops","cat","stop","hat"]
        # ["act", "act"]
        # {"act": [act, cat], "opst": [pots, tops]}
        # Looped through each word and sorted then the words would be the same
        # Check if the words are equal
        hashmap = {}
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            if sorted_word not in hashmap:
                hashmap[sorted_word] = [strs[i]]
                continue
            if sorted_word in hashmap:
                hashmap[sorted_word].append(strs[i])
                continue
        res = []
        for key, value in hashmap.items():
            sublist = []
            for j in range(len(value)):
                sublist.append(value[j])
            res.append(sublist)
        return res
            
            
        
        
        




        