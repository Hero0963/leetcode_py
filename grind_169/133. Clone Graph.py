"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

import collections


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None


        node_copy = Node(node.val, [])
        seen = dict()
        seen[node] = node_copy

        que  = collections.deque()
        que.append(node)
        while que:
            cur_node = que.popleft()
            if not cur_node:
                continue

            for neib in cur_node.neighbors:
                if neib not in seen:
                    neib_copy = Node(neib.val, [])
                    seen[neib] = neib_copy
                    que.append(neib)
                seen[cur_node].neighbors.append(seen[neib])

        return node_copy


# N: number of nodes
# TC: O(N)
# SC: O(N)
