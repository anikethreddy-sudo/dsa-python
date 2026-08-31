def car_fleet(target, position, speed):
    cars = list(zip(position, speed))
    cars.sort(reverse=True)

    stack = []

    for pos, spd in cars:
        time = (target - pos) / spd
        stack.append(time)

        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

print(car_fleet(target, position, speed))
