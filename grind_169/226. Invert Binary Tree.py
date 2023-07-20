# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    N: the number of leaf nodes
    time complexity: O(N)
    space complexity: O(1)

    Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

    Since invertTree returns invertTree, I choose to use a helper function instead of whe way of written self.invertTree
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[invertTree]:
        def helper(root):
            if not root:
                return

            root.left, root.right = root.right, root.left
            helper(root.left)
            helper(root.right)

        head = root
        helper(root)

        return head
