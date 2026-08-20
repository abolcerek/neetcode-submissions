import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x1, y1):
            distance =  math.sqrt(((x1)**2) + ((y1)**2))
            print(distance)
            return distance

        points.sort(key=lambda x: distance(x[0], x[1]))
        return points[:k]