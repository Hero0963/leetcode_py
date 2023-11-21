# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        if not root:
            return self.res

        que = collections.deque()
        que.append(root)
        while que:
            cur_level = []
            for _ in range(len(que)):
                node = que.popleft()
                cur_level.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            self.res.append(cur_level)

        return self.res

# N: number of tree nodes
# TC: O(N)
# SC: O(N)