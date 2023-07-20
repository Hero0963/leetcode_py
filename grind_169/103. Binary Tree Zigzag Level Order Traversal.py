# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# N: number of nodes:
# TC: O(N)
# SC: O(N)

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        cur_level = 0
        que = collections.deque()
        if root:
            que.append(root)

        while que:
            l = len(que)
            vals = []
            for _ in range(l):
                node = que.popleft()
                vals.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            if cur_level % 2 == 1:
                vals.reverse()
            res.append(vals)

            cur_level += 1

        return res
