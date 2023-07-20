import collections
import heapq


# T: len(tasks)
# N: n
# K: number of tasks
# TC: O(T + K + NVlogK)
# SC: O(K)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        total_task = len(tasks)
        cnt = 0
        procedure = []
        counter = collections.Counter(tasks)
        h = []
        for task, val in counter.items():
            heapq.heappush(h, (-val, task))
        # print(h)

        while h:
            # print("procedure = ", procedure)
            tmp = []
            idle_cnt = []
            for _ in range(n + 1):
                if h:
                    v, task = heapq.heappop(h)
                    if v < -1:
                        tmp.append((v + 1, task))
                    procedure.append(task)
                else:
                    idle_cnt.append("idle")

            for ele in tmp:
                heapq.heappush(h, ele)

            if h:
                procedure += idle_cnt

        # print(procedure)

        return len(procedure)


# T: len(tasks)
# N: n
# K: number of tasks
# V: max_val of tasks, i.e. max(counter.values())
# TC: O(T + K + NVlogK)
# SC: O(K)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        procedure = 0
        counter = collections.Counter(tasks)
        h = []
        for task, val in counter.items():
            heapq.heappush(h, (-val, task))

        while h:
            # print("procedure = ", procedure)
            tmp = []
            idle_cnt = 0
            for _ in range(n + 1):
                if h:
                    v, task = heapq.heappop(h)
                    if v < -1:
                        tmp.append((v + 1, task))
                    procedure += 1
                else:
                    idle_cnt += 1

            for ele in tmp:
                heapq.heappush(h, ele)

            if h:
                procedure += idle_cnt

        return procedure


# N: n
# M: len(tasks)
# K: number of tasks, i.e. len(counter)
# TC: O(M + K)
# SC: O(K)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = collections.Counter(tasks).values()
        mx = max(task_counts)
        mx_cnt = list(task_counts).count(mx)
        return max(len(tasks), (mx - 1) * (n + 1) + mx_cnt)
