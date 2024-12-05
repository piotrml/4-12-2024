import time
import tracemalloc
from ctypes import HRESULT
from turtledemo.penrose import start

import numpy as np

# pip install numpy


# tracemalloc.start()
# #array1 = np.arange(10_000_000, dtype=np.int64)
# #array2 = np.arange(10_000_000, dtype=np.int64)
# array3 = np.arange(10_000_000, dtype=np.int32)
# array4 = np.arange(10_000_000, dtype=np.int32)
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f'Current memory usage: {current / 1024 ** 2} MB')
# print(f'Peak memory usage: {peak / 1024 ** 2} MB')
# Current memory usage: 152.58807373046875 MB
# Peak memory usage: 152.58807373046875 MB
#Current memory usage: 76.29412841796875 MB
#Peak memory usage: 76.29412841796875 MB
# tracemalloc.start()
lista1 = list(range(10_000_000))
lista2 = list(range(10_000_000))
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f'Current memory usage: {current / 1024 ** 2} MB')
# print(f'Peak memory usage: {peak / 1024 ** 2} MB')
# Current memory usage: 762.9238739013672 MB
# Peak memory usage: 762.9239807128906 MB

array1 = np.arange(10_000_000)
array2 = np.arange(10_000_000)

def meas_time(func):
    def wrapper(*args, **kwargs):
        start_time =time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        print(f'Czas wykoania funkcji {func.__name__}: {exec_time}')
        return result
    return wrapper

@meas_time
def add_without_np():
    res = [lista1[i] +lista2[i] for i in range(len(lista1))]
    return "OK"
print("Start")
print(add_without_np())

@meas_time
def add_np():
    res = array1 + array2
    return "OK np"
print(add_np())
# Start
# Czas wykoania funkcji add_without_np: 1.7584948539733887
# OK
# Czas wykoania funkcji add_np: 0.053809404373168945
# OK np