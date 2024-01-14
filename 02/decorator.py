"""Decorator"""

import time
from functools import wraps

data_runtimes = {}


def mean(call_count):
    """count mean time of k previous calls of function"""
    def timer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            name_function = func.__name__

            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed_time = time.perf_counter() - start_time
            data_runtimes.setdefault(name_function, [])

            list_executed = data_runtimes[name_function]
            list_executed.append(round(elapsed_time, 10))

            if call_count <= len(list_executed):
                summa = sum(list_executed[len(list_executed) - call_count:])
                print(f"In last {call_count} calls mean executed func time is: ", summa/call_count)
            return result
        return wrapper
    return timer


@mean(5)
def factorial(number):
    """Usual factorial"""
    if number <= 0:
        return None
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact


def compute_factorial(n):
    """compute factorial for n first number"""
    for num in range(1, n):
        print(num, "Result: ", factorial(num))


if __name__ == "__main__":
    compute_factorial(6)
