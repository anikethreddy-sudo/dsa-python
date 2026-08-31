def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev = stack.pop()
            result[prev] = i - prev

        stack.append(i)

    return result


temps = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temperatures(temps))
