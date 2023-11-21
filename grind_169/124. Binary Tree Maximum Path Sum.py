# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -math.inf

        def helper(node):
            if not node:
                return 0

            l_sum = helper(node.left)
            r_sum = helper(node.right)

            l = max(0, l_sum)
            r = max(0, r_sum)

            self.ans = max(self.ans, node.val + l + r)

            return node.val + max(l, r)

        helper(root)
        return self.ans

# N: number of nodes
# TC: O(N)
# SC: O(N)
