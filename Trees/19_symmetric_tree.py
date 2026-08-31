class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):
    def mirror(left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.val != right.val:
            return False

        return (mirror(left.left, right.right) and
                mirror(left.right, right.left))

    if not root:
        return True

    return mirror(root.left, root.right)
