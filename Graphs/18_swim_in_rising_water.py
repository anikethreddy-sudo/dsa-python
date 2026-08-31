import heapq

def swim_in_water(grid):
    n = len(grid)
    visited = set()
    min_heap = [(grid[0][0], 0, 0)]

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while min_heap:
        time, r, c = heapq.heappop(min_heap)

        if (r, c) in visited:
            continue

        visited.add((r, c))

        if r == n - 1 and c == n - 1:
            return time

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                heapq.heappush(
                    min_heap,
                    (max(time, grid[nr][nc]), nr, nc)
                )


grid = [
    [0, 2],
    [1, 3]
]

print(swim_in_water(grid))
