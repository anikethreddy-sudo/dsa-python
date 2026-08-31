import heapq

def network_delay_time(times, n, k):
    graph = {}

    for u, v, w in times:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

    min_heap = [(0, k)]
    visited = {}

    while min_heap:
        time, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited[node] = time

        if node in graph:
            for nei, weight in graph[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (time + weight, nei))

    if len(visited) == n:
        return max(visited.values())

    return -1


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

print(network_delay_time(times, n, k))
