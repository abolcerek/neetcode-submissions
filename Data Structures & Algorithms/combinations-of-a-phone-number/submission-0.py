class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        characters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def dfs(i, substr):
            if len(substr) >= len(digits):
                res.append(substr)
                return
            for c in characters[digits[i]]:
                dfs(i + 1, substr + c)
        dfs(0, "")
        return res