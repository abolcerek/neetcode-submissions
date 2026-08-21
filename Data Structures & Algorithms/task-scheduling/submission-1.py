import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        res = [-cnt for cnt in count.values()]
        heapq.heapify(res)

        time = 0
        queue = deque()

        while res or queue:
            time += 1
            if res:
                cnt = 1 + heapq.heappop(res)
                if cnt:
                    queue.append([cnt, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(res, queue.popleft()[0])

        return time

    