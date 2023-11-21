# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = -1
        self.cnt = 0

        def helper(node):
            if not node:
                return

            helper(node.left)

            self.cnt += 1
            if self.cnt == k:
                self.ans = node.val
                return

            helper(node.right)

        helper(root)

        return self.ans

# N: number of treenodes
# H: height of tree
# TC: O(K)
# SC: O(H), H for helper, recursive function calls need H stacks
