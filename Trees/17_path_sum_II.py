class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root, target_sum):
    result = []

    def dfs(node, remaining, path):
        if not node:
            return

        path.append(node.val)
        remaining -= node.val

        if not node.left and not node.right and remaining == 0:
            result.append(path[:])

        dfs(node.left, remaining, path)
        dfs(node.right, remaining, path)

        path.pop()

    dfs(root, target_sum, [])
    return result
