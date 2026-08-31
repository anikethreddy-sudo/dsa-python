def find_redundant_connection(edges):
    parent = [i for i in range(len(edges) + 1)]

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        rootA = find(a)
        rootB = find(b)

        if rootA == rootB:
            return False

        parent[rootA] = rootB
        return True

    for u, v in edges:
        if not union(u, v):
            return [u, v]


edges = [[1,2], [1,3], [2,3]]
print(find_redundant_connection(edges))
