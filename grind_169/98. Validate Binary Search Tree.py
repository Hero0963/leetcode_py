# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# N: number of nodes
# TC: O(N)
# SC: O(1)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower_bound, upper_bound):
            if not node:
                return True

            if not lower_bound < node.val < upper_bound:
                return False

            return helper(node.left, lower_bound, node.val) and helper(node.right, node.val, upper_bound)

        return helper(root, float("-inf"), float("inf"))
