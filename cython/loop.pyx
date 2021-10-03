# distutils: language=c++
# cython: language_level=3
import time

cpdef loop():
    for _ in range(10_000_000):
        continue
