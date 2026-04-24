from python.basic_algorithm.tree import BinaryTree, SegmentTree, TreeNode
from python.basic_algorithm.tree_traversal import Traversal


def create_sample_tree():
    tree = BinaryTree()
    root = TreeNode(1)
    tree.root = root
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.left.left.left = TreeNode(6)
    return tree


def test_height():
    tree = BinaryTree()
    tree.root = None
    root = TreeNode(1)
    tree.root = root
    assert tree.height() == 1
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert tree.height() == 2
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    assert tree.height() == 4
    root.right.left = TreeNode(6)
    assert tree.height() == 4


def test_is_balanced():
    tree = BinaryTree()
    assert tree.is_balanced()
    root = TreeNode(1)
    tree.root = root
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    assert tree.is_balanced()
    root.left.left.left = TreeNode(5)
    root.right.left = TreeNode(6)
    assert not tree.is_balanced()


def test_preorder_traverse():
    tree = create_sample_tree()
    traversal = Traversal(tree.root)
    assert traversal.preorder() == [1, 2, 4, 6, 3, 5]
    traversal = Traversal(None)
    assert traversal.preorder() == []


def test_inorder_traverse():
    tree = create_sample_tree()
    traversal = Traversal(tree.root)
    assert traversal.inorder() == [6, 4, 2, 1, 5, 3]


def test_postorder_traverse():
    tree = create_sample_tree()
    traversal = Traversal(tree.root)
    assert traversal.postorder() == [6, 4, 2, 5, 3, 1]


def test_segment_tree():
    tree = SegmentTree([0, 2, 3, 4, 5])
    assert tree.query(1, 3) == 9
    tree.update(1, 2)
    assert tree.query(1, 3) == 11
    assert tree.query(0, 0) == 0
    assert tree.query(-1, -1) == 0
