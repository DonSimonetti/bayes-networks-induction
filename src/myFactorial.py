cached_values = [1]


def generate_factorials(size):
    cached_values.clear()
    cached_values.append(1)
    for i in range(size):
        cached_values.append(cached_values[i] * (i + 1))


def factorial(value):
    if len(cached_values) - 1 < value:
        generate_factorials(value)
    return cached_values[value]

