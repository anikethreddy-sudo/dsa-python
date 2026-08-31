import heapq

def find_cheapest_price(n, flights, src, dst, k):
    graph = {}

    for u, v, price in flights:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, price))

    heap = [(0, src, 0)]  # cost, city, stops
    visited = {}

    while heap:
        cost, city, stops = heapq.heappop(heap)

        if city == dst:
            return cost

        if stops > k:
            continue

        if (city, stops) in visited and visited[(city, stops)] <= cost:
            continue

        visited[(city, stops)] = cost

        if city in graph:
            for nxt, price in graph[city]:
                heapq.heappush(heap, (cost + price, nxt, stops + 1))

    return -1


n = 4
flights = [[0,1,100],[1,2,100],[2,3,100],[0,2,500]]
src = 0
dst = 3
k = 1

print(find_cheapest_price(n, flights, src, dst, k))
