# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# N: the number of nodes
# TC: O(N)
# SC: O(N)
import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []

        def helper(node, level):
            if not node:
                return

            if len(self.res) <= level:
                self.res.append([node.val])
            else:
                self.res[level].append(node.val)

            helper(node.left, level + 1)
            helper(node.right, level + 1)

        helper(root, 0)

        return self.res




# N: the number of nodes
# TC: O(N)
# SC: O(N)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []

        if not root:
            return self.res

        q = collections.deque()
        q.append(root)
        while q:
            cur_level = []
            for _ in range(len(q)):
                node = q.popleft()
                cur_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            self.res.append(cur_level)

        return self.res