class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same(a, b):
    if not a and not b:
        return True

    if not a or not b:
        return False

    if a.val != b.val:
        return False

    return is_same(a.left, b.left) and is_same(a.right, b.right)


def is_subtree(root, sub_root):
    if not sub_root:
        return True

    if not root:
        return False

    if is_same(root, sub_root):
        return True

    return (is_subtree(root.left, sub_root) or
            is_subtree(root.right, sub_root))
