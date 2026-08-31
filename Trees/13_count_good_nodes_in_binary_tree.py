class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def good_nodes(root):
    def dfs(node, max_value):
        if not node:
            return 0

        count = 1 if node.val >= max_value else 0
        max_value = max(max_value, node.val)

        count += dfs(node.left, max_value)
        count += dfs(node.right, max_value)

        return count

    return dfs(root, root.val)
