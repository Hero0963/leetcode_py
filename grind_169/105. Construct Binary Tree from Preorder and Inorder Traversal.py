# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        record_idx = {val: i for i, val in enumerate(inorder)}

        self.pre_index = 0

        def helper(start: int, end: int) -> TreeNode:
            if start > end:
                return None

            val = preorder[self.pre_index]
            self.pre_index += 1
            mid = record_idx[val]

            node = TreeNode()
            node.val = val
            node.left = helper(start, mid - 1)
            node.right = helper(mid + 1, end)

            return node

        root = helper(0, n - 1)
        return root

# N: len(inorder)
# TC: O(N)
# SC: O(N)
# by @netotz
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/34579/python-short-recursive-solution/
