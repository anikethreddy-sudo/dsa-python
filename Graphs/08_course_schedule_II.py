from collections import deque

def find_order(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque()

    for i in range(num_courses):
        if indegree[i] == 0:
            queue.append(i)

    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) == num_courses:
        return order

    return []


num_courses = 4
prerequisites = [[1,0], [2,0], [3,1], [3,2]]

print(find_order(num_courses, prerequisites))
