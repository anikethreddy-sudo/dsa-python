from collections import deque

def can_finish(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque()

    for i in range(num_courses):
        if indegree[i] == 0:
            queue.append(i)

    completed = 0

    while queue:
        course = queue.popleft()
        completed += 1

        for neighbor in graph[course]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return completed == num_courses


num_courses = 2
prerequisites = [[1, 0]]

print(can_finish(num_courses, prerequisites))
