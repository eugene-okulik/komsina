def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_nth_number(generator, n):
    fibonacci_number = 0

    for i in range(n + 1):
        fibonacci_number = next(generator)
    return fibonacci_number


print(f"{get_nth_number(fibonacci_generator(), 4)}")
print(f"{get_nth_number(fibonacci_generator(), 199)}")
print(f"{get_nth_number(fibonacci_generator(), 999)}")
print(f"{get_nth_number(fibonacci_generator(), 99999)}")
