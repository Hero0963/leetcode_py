# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node: Optional[TreeNode], lower_bound: int = float("-inf"), upper_bound: int = float("inf")) -> bool:
            if not node:
                return True

            if not lower_bound < node.val < upper_bound:
                return False

            return helper(node.left, lower_bound, node.val) and helper(node.right, node.val, upper_bound)

        return helper(root, float("-inf"), float("inf"))

# N: number of tree nodes
# TC: O(N)
# SC: O(N)
