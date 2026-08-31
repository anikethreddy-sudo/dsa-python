from collections import deque

def open_lock(deadends, target):
    dead = set(deadends)

    if "0000" in dead:
        return -1

    queue = deque([("0000", 0)])
    visited = {"0000"}

    while queue:
        lock, turns = queue.popleft()

        if lock == target:
            return turns

        for i in range(4):
            digit = int(lock[i])

            for move in (-1, 1):
                new_digit = (digit + move) % 10
                new_lock = lock[:i] + str(new_digit) + lock[i+1:]

                if new_lock not in dead and new_lock not in visited:
                    visited.add(new_lock)
                    queue.append((new_lock, turns + 1))

    return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"

print(open_lock(deadends, target))
