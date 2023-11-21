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

# BFS solution ref = https://leetcode.com/problems/serialize-and-deserialize-binary-tree/solutions/314218/python-bfs-and-dfs-solutions/
# by @otoc
"""
class Codec:
    def serialize(self, root):
        if not root:
            return []
        lst, curr_level = [], [root]
        while curr_level:
            next_level, has_value = [], False
            for node in curr_level:
                if node:
                    lst.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
                    if node.left or node.right:
                        has_value = True
                else:
                    lst.append(None)
            curr_level = next_level if has_value else []
        return lst

    def deserialize(self, data):
        n = len(data)
        if n == 0:
            return None
        root = TreeNode(data[0])
        curr_level, i = [root], 1
        while curr_level and i < n:
            next_level = []
            for node in curr_level:
                if data[i] != None:
                    node.left = TreeNode(data[i])
                    next_level.append(node.left)
                i += 1
                if data[i] != None:
                    node.right = TreeNode(data[i])
                    next_level.append(node.right)
                i += 1
            curr_level = next_level
        return root
"""
