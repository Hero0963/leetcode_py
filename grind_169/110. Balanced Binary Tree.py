# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height_unbalanced = -1

        def get_height(node):
            if not node:
                return 0

            l, r = get_height(node.left), get_height(node.right)
            if abs(l - r) > 1:
                return height_unbalanced
            if l == height_unbalanced or r == height_unbalanced:
                return height_unbalanced

            return 1 + max(l, r)

        res = get_height(root)
        return res != height_unbalanced

# N: number of tree nodes:
# H: height of tree
# TC: O(N)
# SC: O(H)