# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        self.record = collections.defaultdict(int)
        self.tagert = targetSum

        def dfs(node, pre_sum):
            if not node:
                return

            cur_sum = pre_sum + node.val
            diff = cur_sum - self.tagert
            self.ans += self.record[diff]
            self.record[cur_sum] += 1
            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)
            self.record[cur_sum] -= 1

        self.record[0] = 1
        dfs(root, 0)
        return self.ans

# N: number of Treenodes
# TC: O(N)
# SC: O(N)
# ref = https://leetcode.com/problems/path-sum-iii/solutions/170367/python-solution/
