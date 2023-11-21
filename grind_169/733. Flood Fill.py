import collections


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ori_color = image[sr][sc]
        if ori_color == color:
            return image

        n, m = len(image), len(image[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        que = collections.deque()
        que.append((sr, sc))
        while que:
            x, y = que.popleft()
            image[x][y] = color
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and image[nx][ny] == ori_color:
                    que.append((nx, ny))

        return image

# N: len(image)
# M: len(image[0])
# TC: O(N * M)
# SC: O(N * M)
