# Getting started with Numpy
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(type(arr))

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

print(dir(arr))

print(np.shape(arr))

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(d.shape)