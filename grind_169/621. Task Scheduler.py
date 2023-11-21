class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = collections.Counter(tasks).values()
        mx = max(task_counts)
        mx_cnt = list(task_counts).count(mx)
        return max(len(tasks), (mx - 1) * (n + 1) + mx_cnt)

# N: n
# T: len(tasks)
# C: number of tasks, i.e. len(counter)
# TC: O(T + C)
# SC: O(C)
