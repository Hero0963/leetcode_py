# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections


# N: number of TreeNodes
# L: level of Tree
# TC: O(N)
# SC: O(2^L)

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que = collections.deque()
        que.append((root, 0))
        res = 0

        while que:
            l = len(que)
            _, left_idx = que[0]
            _, right_idx = que[-1]
            # print("left_idx, right_idx ", left_idx, right_idx)
            res = max(res, right_idx - left_idx + 1)
            for _ in range(l):
                node, idx = que.popleft()
                if node.left:
                    que.append((node.left, idx * 2 + 1))
                if node.right:
                    que.append((node.right, idx * 2 + 2))

        return res
