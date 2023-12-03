# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(node1, node2):
            if not node1 and not node2:
                return True
            if not (node1 and node2):
                return False
            if node1.val != node2.val:
                return False

            return is_same_tree(node1.left, node2.left) and is_same_tree(node1.right, node2.right)

        que = deque()
        que.append(root)
        while que:
            l = len(que)
            for _ in range(l):
                q = que.popleft()
                if is_same_tree(q, subRoot):
                    return True
                if q:
                    que.append(q.left)
                    que.append(q.right)
        return False

# N: number of treenodes in root
# M: number of treenodes in subRoot
# TC: O(MN)
# SC: O(M + N)
# ref = https://leetcode.cn/problems/subtree-of-another-tree/solutions/233896/ling-yi-ge-shu-de-zi-shu-by-leetcode-solution/
# @小红帽 竟然用一个题涵盖KMP DFS HASH 埃氏筛选法 收藏从未停止 学习从未开始
