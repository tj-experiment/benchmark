# distutils: language=c++
# cython: language_level=3
import time

def loop():
    start = time.monotonic_ns()
    for i in range(10_000_000):
        continue

    end = time.monotonic_ns()
    elapsed = end - start//1000000

    print(f"Took: {elapsed} milliseconds")

    return elapsed