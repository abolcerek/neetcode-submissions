class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            hashmap[crs].append(pre)

        res = []
        visit = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in hashmap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res