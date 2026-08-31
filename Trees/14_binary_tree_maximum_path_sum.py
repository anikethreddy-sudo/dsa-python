class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root):
    maximum = float("-inf")

    def dfs(node):
        nonlocal maximum

        if not node:
            return 0

        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)

        maximum = max(maximum, node.val + left + right)

        return node.val + max(left, right)

    dfs(root)
    return maximum
