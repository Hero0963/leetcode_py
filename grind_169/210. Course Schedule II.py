import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            g[b].append(a)
            indegrees[a] += 1

        que = collections.deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                que.append(i)

        res = []
        while que:
            l = len(que)
            for _ in range(l):
                x = que.popleft()
                res.append(x)
                for c in g[x]:
                    indegrees[c] -= 1
                    if indegrees[c] == 0:
                        que.append(c)

        if len(res) != numCourses:
            return []

        return res

# N: numCourses
# M: len(prerequisites), M <= N^2
# TC: O(M + N + M)
# SC: O(M + N)
