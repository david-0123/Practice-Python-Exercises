def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    sequence = [1, 1]
    for i in range(2, n):
        nextNum = sequence[-1] + sequence[-2]
        sequence.append(nextNum)

    return sequence

num = int(input('Enter a number: '))
print(fibonacci(num))