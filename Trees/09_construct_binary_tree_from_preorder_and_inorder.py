class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    index_map = {value: i for i, value in enumerate(inorder)}
    preorder_index = 0

    def dfs(left, right):
        nonlocal preorder_index

        if left > right:
            return None

        root_value = preorder[preorder_index]
        preorder_index += 1

        root = TreeNode(root_value)
        mid = index_map[root_value]

        root.left = dfs(left, mid - 1)
        root.right = dfs(mid + 1, right)

        return root

    return dfs(0, len(inorder) - 1)
