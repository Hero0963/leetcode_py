# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# N: number of nodes
# TC: O(N)
# SC: O(N), # worst case for recursive stack


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []

        def helper(node, cur_sum, cur_path):
            if not node:
                return

            cur_sum += node.val
            cur_path.append(node.val)

            if not node.left and not node.right and cur_sum == targetSum:
                self.res.append(cur_path[:])

                cur_path.pop()
                return

            helper(node.left, cur_sum, cur_path)
            helper(node.right, cur_sum, cur_path)

            cur_path.pop()
            return

        helper(root, 0, [])

        return self.res
