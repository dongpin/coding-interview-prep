"""
    Problems about tree traversals
"""

from collections import deque


class Traversal:
    def __init__(self, root):
        self.root = root

    def preorder(self):
        res = []

        def preorder_helper(node):
            if node:
                res.append(node.data)
                preorder_helper(node.left)
                preorder_helper(node.right)
        preorder_helper(self.root)
        return res

    def inorder(self):
        res = []

        def inorder_helper(node):
            if node:
                inorder_helper(node.left)
                res.append(node.data)
                inorder_helper(node.right)
        inorder_helper(self.root)
        return res

    def postorder(self):
        res = []

        def postorder_helper(node):
            if node:
                postorder_helper(node.left)
                postorder_helper(node.right)
                res.append(node.data)
        postorder_helper(self.root)
        return res

    # BFS or Level order traversal
    def bfs(self):
        queue = deque([self.root])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

    def iddfs(self):
        pass

    def morris(self):
        pass
