# ref = leetcode sample code
# V: course node
# E: edge
# TC: O(V+E)
# SC: O(V+E)
# Overall this is an O(N) algorithm, by @kevinhynes

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)

        visited = [0] * numCourses

        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True
            visited[node] = -1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 1
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True


# ref = https://leetcode.com/problems/course-schedule/solutions/162743/java-c-python-bfs-topological-sorting-o-n-e/
# rewrite by @lenchen1112
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = [[] for i in range(numCourses)]
        degrees = [0] * numCourses
        for course, pre_course in prerequisites:
            edges[pre_course].append(course)
            degrees[course] += 1

        queue = collections.deque(course for course, degree in enumerate(degrees) if not degree)
        while queue:
            course = queue.popleft()
            for next_course in edges[course]:
                degrees[next_course] -= 1
                if not degrees[next_course]:
                    queue.append(next_course)

        return not sum(degrees)
