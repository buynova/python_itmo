# Фибоначчи


def fibonacci_generator(n):
    l = list()
    l.append(1)
    l.append(1)
    for i in range(2, n):
        l.append(l[i-1] + l[i-2])

    for item in l:
        yield item

for i in fibonacci_generator(10):
    print(i)
