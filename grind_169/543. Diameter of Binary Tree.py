# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        self._diam = 0

        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            self._diam = max(self._diam, left + right)
            return 1 + max(left, right)

        _ = helper(root)
        return self._diam

# N: number of tree nodes
# TC: O(N)
# SC: O(N)
# ref = https://www.youtube.com/watch?v=UfPMw8zD8EY, treat each node as a inflection point
