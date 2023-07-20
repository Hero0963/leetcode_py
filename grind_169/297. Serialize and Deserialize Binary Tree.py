# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.ans = []

        def dfs(node):
            if not node:
                self.ans.append("#")
                return
            self.ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return " ".join(self.ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper(q):
            if q[0] == "#":
                q.popleft()
                return None
            node = TreeNode(int(q.popleft()))
            l = helper(q)
            r = helper(q)
            node.left = l
            node.right = r
            return node

        que = collections.deque(data.split())
        return helper(que)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))