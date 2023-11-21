# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


# N: number of nodes
# TC: O(N)
# SC: O(N)

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        node = root

        def build_graph(node):
            if not node:
                return

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)

            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)

            build_graph(node.left)
            build_graph(node.right)

        build_graph(root)

        que = deque()
        que.append(target)
        seen = set()
        distance = 0
        while que:
            if distance == k:
                break

            l = len(que)
            for _ in range(l):
                node = que.popleft()
                if node in seen:
                    continue

                seen.add(node)
                adj_list = graph[node]
                for adj in adj_list:
                    if adj not in seen:
                        que.append(adj)

            distance += 1

        ans = []
        for node in que:
            if node not in seen:
                ans.append(node.val)
                seen.add(node)
        return ans
