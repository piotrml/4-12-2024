import time
import tracemalloc
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
# lista1 = list(range(10_000_000))
# lista2 = list(range(10_000_000))
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f'Current memory usage: {current / 1024 ** 2} MB')
# print(f'Peak memory usage: {peak / 1024 ** 2} MB')
# Current memory usage: 762.9238739013672 MB
# Peak memory usage: 762.9239807128906 MB

array1 = np.arange(10_000_000)
array2 = np.arange(10_000_000)