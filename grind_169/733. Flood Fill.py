# ref = https://leetcode.com/problems/flood-fill/solutions/109604/easy-python-dfs-no-need-for-visited/
# note: There is a tricky case where the new color is the same as the original color and if the DFS is done on it, there will be an infinite loop.


class Solution:
    """
    N = len(image)
    M = len(image[0])

    time complexity: O(N * M)
    space complexity: O(N * M)

    Constraints:

    m == image.length
    n == image[i].length
    1 <= m, n <= 50
    0 <= image[i][j], color < 216
    0 <= sr < m
    0 <= sc < n

    """

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        ori_color = image[sr][sc]
        n = len(image)
        m = len(image[0])

        # visited = [[False for _ in range(m)] for _ in range(n) ]

        def dfs(r: int, c: int):
            # if visited[r][c]:
            #     return

            # visited[r][c] = True

            if image[r][c] != ori_color:
                return

            image[r][c] = color

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for d in directions:
                x, y = r + d[0], c + d[1]

                if x < 0 or x >= n or y < 0 or y >= m:
                    continue

                dfs(x, y)

        if ori_color != color:
            dfs(sr, sc)

        return image
