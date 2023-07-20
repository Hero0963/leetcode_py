# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    H : depth of root
    time complexity: O(2^H)
    space complexity: O(1)

    Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -10^4 <= Node.val <= 10^4

    """

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            if not node:
                return 0

            l, r = get_height(node.left), get_height(node.right)
            if abs(l - r) > 1:
                return -1
            if l == -1 or r == -1:
                return -1

            return 1 + max(l, r)

        res = get_height(root)

        return True if res >= 0 else False
