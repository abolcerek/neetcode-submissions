class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0) #adding 0 to the end of the array

        for i in range(len(cost) - 3, -1, -1): #we decrement from the position in the array where the element's second step climbs to the top of the stairs
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2]) #we store in the index of the element the minimum cost of steps it can take
        return min(cost[0], cost[1]) #we return the minimum of either index 0 or index 1 which will have the least amount of steps stored in the index