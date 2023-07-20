# N: number of treenode
# TC: O(N)
# SC: O(N)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        cur_level = []
        cur_level.append(root)
        while True:
            l = len(cur_level)
            nxt_level = []
            saw_it = False
            for _ in range(l):
                node = cur_level.pop()

                if not node:
                    continue

                if not saw_it:
                    ans.append(node.val)
                    saw_it = True

                nxt_level.append(node.right)
                nxt_level.append(node.left)

            cur_level = nxt_level[::-1]
            if not cur_level:
                break

        return ans


# N: number of treenode
# TC: O(N)
# SC: O(N)

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
