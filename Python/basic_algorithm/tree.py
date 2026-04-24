"""
    Tree
"""

from collections import namedtuple, deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

# Binary Tree


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    # Height of root node is number of edges from bottom
    # Depth of root node is 0
    def height(self):
        def height_helper(node):
            if not node:
                return 0
            return max(height_helper(node.left), height_helper(node.right)) + 1
        return height_helper(self.root)

    def height_iterative(self):
        if not self.root:
            return 0
        queue = deque([self.root])
        height = 0
        while queue:
            size = len(queue)
            while size:
                size -= 1
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            height += 1
        return height

    # Approach 1: recursively check if comply with bst property
    # Approach 2: inorder traversal
    def is_bst(self):
        def is_bst_helper(node, low, high):
            if not node:
                return True
            if node.data < low or node.data > high:
                return False
            return is_bst_helper(node.left, low, node.data) \
                and is_bst_helper(node.right, node.data, high)
        return is_bst_helper(self.root, float('-inf'), float('inf'))

    def is_bst_inorder(self):
        prev = [None]

        def inorder(node):
            if node:
                if not inorder(node.left):
                    return False
                if prev[0] is not None and node.data <= prev[0]:
                    return False
                prev[0] = node.data
                if not inorder(node.right):
                    return False
            return True
        return inorder(self.root)

    def is_balanced(self):
        BalancedStatusWithHeight = namedtuple(
            'BalancedStatusWithHeight', ('balanced', 'height'))

        def check_balanced(tree):
            if not tree:
                return BalancedStatusWithHeight(True, -1)
            left = check_balanced(tree.left)
            if not left.balanced:
                return BalancedStatusWithHeight(False, 0)
            right = check_balanced(tree.right)
            if not right.balanced:
                return BalancedStatusWithHeight(False, 0)

            is_balanced = abs(left.height - right.height) <= 1
            height = max(left.height, right.height) + 1
            return BalancedStatusWithHeight(is_balanced, height)
        return check_balanced(self.root).balanced

    def is_symmetric(self):
        def check_symmetric(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if tree1 and tree2 and tree1.data == tree2.data:
                return check_symmetric(tree1.left, tree2.left) \
                    and check_symmetric(tree1.right, tree2.right)
            return False
        if not self.root:
            return True
        return check_symmetric(self.root.left, self.root.right)

# Binary Search Tree


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def search(self, key):
        def search_helper(node, key):
            if not node:
                return None
            if key == node.data:
                return node
            elif key < node.data:
                return search_helper(node.left, key)
            else:
                return search_helper(node.right, key)
        return search_helper(self.root, key)

    def search_iterative(self, key):
        node = self.root
        while node:
            if node.data == key:
                return node
            if node.data < key:
                node = node.right
            elif node.data > key:
                node = node.left
        return None

    def insert(self, data):
        def insert_helper(root, node):
            if root is None:
                root = node
            elif node.data <= root.data:
                if root.left is None:
                    root.left = node
                else:
                    insert_helper(root.left, node)
            else:
                if root.right is None:
                    root.right = node
                else:
                    insert_helper(root.right, node)
        node = TreeNode(data)
        insert_helper(self.root, node)

    def delete(self, key):
        def delete_helper(root, key):
            if not root:
                return None
            if key < root.data:
                root.left = delete_helper(root.left, key)
            elif key > root.data:
                root.right = delete_helper(root.right, key)
            else:
                # only one child or no child
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left

                # has two children: get the inorder successor
                current = root.right
                while current.left:
                    current = current.left
                root.data = current.data
                root.right = delete_helper(root.right, current.data)
            return root
        self.root = delete_helper(self.root, key)

    def size(self):
        pass

    def max(self):
        pass

    def min(self):
        pass

    # The most important points is, BFS starts visiting nodes from root
    # while DFS starts visiting nodes from leaves.
    # So if our problem is to search something that is more likely to closer to root,
    # we would prefer BFS. And if the target node is close to a leaf, we would
    # prefer DFS.
    def printAllLeaves(self):
        pass

    def printKthLevel(self, k):
        pass

# Self-balanced BST


class SelfBalancingBST:
    pass

# Red-Black Tree


class RBTree(SelfBalancingBST):
    pass

# AVL Tree


class AVLTree(SelfBalancingBST):
    pass

# Splay Tree


class SplayTree(SelfBalancingBST):
    pass

# 2-3 search trees


class TwoThreeSearchTree:
    pass

# Finger Tree https://zhuanlan.zhihu.com/p/30589105


class FingerTree:
    pass

# Segment Tree


class SegementTreeNode:
    def __init__(self, start, end, value):
        self.start = start
        self.end = end
        self.val = value
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.root = self.build_tree(0, len(self.arr) - 1)

    def build_tree(self, lo, hi):
        if lo == hi:
            return SegementTreeNode(lo, hi, self.arr[lo])
        mid = lo + (hi - lo) // 2
        left = self.build_tree(lo, mid)
        right = self.build_tree(mid + 1, hi)
        root = SegementTreeNode(lo, hi, left.val + right.val)
        root.left, root.right = left, right
        return root

    def _query(self, node, start, end):
        mid = node.start + (node.end - node.start) // 2
        if start <= node.start and node.end <= end:
            return node.val
        elif end <= mid:
            return self._query(node.left, start, end)
        elif start > mid:
            return self._query(node.right, start, end)
        elif start <= mid and mid < end:
            return self._query(node.left, start, mid) + \
                self._query(node.right, mid + 1, end)
        return 0

    def query(self, start, end):
        if start < 0 or end > len(self.arr) - 1:
            return 0
        return self._query(self.root, start, end)

    def _update(self, i, diff, node):
        if i < node.start or i > node.end:
            return
        node.val += diff
        if node.start == node.end == i:
            return
        self._update(i, diff, node.left)
        self._update(i, diff, node.right)

    def update(self, i, diff):
        self._update(i, diff, self.root)


# Fenwick Tree and Binary Indexed Tree
