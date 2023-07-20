# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# N: number of nodes in TreeNode
# TC: O(N)
# SC: O(1)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def helper(node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> int:
            if not node:
                return 0

            cnt = 0
            if node == p or node == q:
                cnt += 1

            cnt += helper(node.left, p, q) + helper(node.right, p, q)
            if cnt == 2 and self.ans == None:
                self.ans = node

            return cnt

        _ = helper(root, p, q)

        return self.ans
