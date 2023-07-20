# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# ref = https://fuxuemingzhu.cn/leetcode/437.html#%E9%A2%98%E7%9B%AE%E6%8F%8F%E8%BF%B0
# N: number of nodes
# L: Level of treenode, L <= N
# TC: O(N^2)
# SC: O(N), for recursive stack

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        cnt = self.dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        return cnt

    def dfs(self, node, cur_target):
        res = 0
        if not node:
            return res

        cur_target -= node.val
        if cur_target == 0:
            res += 1

        res += self.dfs(node.left, cur_target)
        res += self.dfs(node.right, cur_target)
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# ref = https://leetcode.com/problems/path-sum-iii/solutions/170367/python-solution/
# N: number of TreeNodes
# TC: O(N)
# SC: O(N)


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
