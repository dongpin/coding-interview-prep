"""
    173. Binary search tree iterator
"""


class BstIterator:
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        if self.hasNext():
            res = self.stack.pop()
            node = res.right
            while node:
                self.stack.append(node)
                node = node.left
            return res
        return None

    def hasNext(self):
        return len(self.stack) > 0

    def current(self):
        if self.hasNext():
            return self.stack[-1]
        return None
