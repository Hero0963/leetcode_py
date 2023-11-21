class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        if not root:
            return ans

        deq = deque()
        deq.append(root)

        while deq:
            l = len(deq)
            for _ in range(l):
                node = deq.popleft()
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)

            ans.append(node.val)

        return ans

# N: number of treenode
# TC: O(N)
# SC: O(N)
