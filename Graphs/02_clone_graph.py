class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


def clone_graph(node):
    if not node:
        return None

    copies = {}

    def dfs(curr):
        if curr in copies:
            return copies[curr]

        copy = Node(curr.val)
        copies[curr] = copy

        for neighbor in curr.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node)
