# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq as hq


# N: number of treenodes
# H: the height of tree
# TC: (N + NlogK)
# SC: O(H)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.vals = []

        def helper(node):
            if not node:
                return

            self.vals.append(node.val)

            helper(node.left)
            helper(node.right)

        helper(root)
        hq.heapify(self.vals)
        cnt = 0
        while cnt < k:
            ans = hq.heappop(self.vals)
            cnt += 1

        return ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# N: number of treenodes
# H: height of tree
# TC: O(N)
# SC: O(N + H), H for helper, recursive function calls need H stacks

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.vals = []

        def helper(node):
            if not node:
                return

            helper(node.left)
            self.vals.append(node.val)
            helper(node.right)

        helper(root)
        ans = self.vals[k - 1]

        return ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# N: number of treenodes
# H: height of tree
# TC: O(K)
# SC: O(H), H for helper, recursive function calls need H stacks

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = -1
        self.cnt = 0

        def helper(node):
            if not node:
                return

            helper(node.left)

            self.cnt += 1
            if self.cnt == k:
                self.ans = node.val
                return

            helper(node.right)

        helper(root)

        return self.ans
