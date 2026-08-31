from collections import defaultdict

def find_itinerary(tickets):
    graph = defaultdict(list)

    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)

    itinerary = []

    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop()
            dfs(next_airport)

        itinerary.append(airport)

    dfs("JFK")
    return itinerary[::-1]


tickets = [
    ["MUC", "LHR"],
    ["JFK", "MUC"],
    ["SFO", "SJC"],
    ["LHR", "SFO"]
]

print(find_itinerary(tickets))
