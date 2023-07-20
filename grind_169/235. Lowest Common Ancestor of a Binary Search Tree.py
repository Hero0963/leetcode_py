# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    N = depth of root
    time complexity: O(N)
    space complexity: O(1)

    Constraints:

    The number of nodes in the tree is in the range [2, 105].
    -10^9 <= Node.val <= 10^9
    All Node.val are unique.
    p != q
    p and q will exist in the BST.
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p

        node = root
        while node:
            if p.val <= node.val <= q.val:
                return node
            elif node.val > q.val:
                node = node.left
            elif node.val < p.val:
                node = node.right
            else:
                return root

        return root
