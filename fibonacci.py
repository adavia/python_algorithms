def fibonacci(n):
    a = 0
    b = 1

    while a < n:
        yield a
        future = a + b
        a = b
        b = future

        # Same as a, b = b, a + b

for num in fibonacci(8):
    print(num)
