"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


# TC: O(V + E)
# SC: O(V + E)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        node_copy = self.dfs(node, dict())
        return node_copy

    def dfs(self, node: 'Node', hash_map: dict) -> 'Node':
        if not node:
            return None

        if node in hash_map:
            return hash_map[node]

        node_copy = Node(node.val, [])
        hash_map[node] = node_copy

        for n in node.neighbors:
            n_copy = self.dfs(n, hash_map)
            if n_copy:
                node_copy.neighbors.append(n_copy)

        return node_copy


import collections


# TC: O(V + E)
# SC: O(V + E)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        que = collections.deque()
        hash_map = dict()
        que.append(node)
        node_copy = Node(node.val, [])
        hash_map[node] = node_copy

        while que:
            q = que.popleft()
            if not q:
                continue
            for n in q.neighbors:
                if n not in hash_map:
                    hash_map[n] = Node(n.val, [])
                    que.append(n)
                hash_map[q].neighbors.append(hash_map[n])

        return node_copy
