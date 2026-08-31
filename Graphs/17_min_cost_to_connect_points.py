import heapq

def min_cost_connect_points(points):
    n = len(points)
    visited = set()
    min_heap = [(0, 0)]
    cost = 0

    while len(visited) < n:
        weight, i = heapq.heappop(min_heap)

        if i in visited:
            continue

        visited.add(i)
        cost += weight

        x1, y1 = points[i]

        for j in range(n):
            if j not in visited:
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(min_heap, (dist, j))

    return cost


points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(min_cost_connect_points(points))
