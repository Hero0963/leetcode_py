# ref = https://fuxuemingzhu.cn/leetcode/310.html#bfs
# ref = https://github.com/wisdompeak/LeetCode/blob/master/BFS/310.Minimum-Height-Trees/310.Minimum-Height-Trees.py


# N: n
# M: len(edges)
# TC: O(M)
# SC: O(N + M)

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        degree = [0] * n
        neighbor = [[] for _ in range(n)]

        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            neighbor[u].append(v)
            neighbor[v].append(u)

        que = collections.deque()
        for i in range(n):
            if degree[i] == 1:
                que.append(i)

        cnt = 0
        while que:
            l = len(que)
            for _ in range(l):
                x = que.popleft()
                cnt += 1
                for y in neighbor[x]:
                    degree[y] -= 1
                    if degree[y] == 1:
                        que.append(y)

            if cnt + len(que) == n:
                ans = list(que)
                return ans
