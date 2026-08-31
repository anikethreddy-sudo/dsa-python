def count_components(n, edges):
    graph = {i: [] for i in range(n)}

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    components = 0

    def dfs(node):
        if node in visited:
            return

        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)

    for i in range(n):
        if i not in visited:
            components += 1
            dfs(i)

    return components


n = 5
edges = [[0,1], [1,2], [3,4]]

print(count_components(n, edges))
