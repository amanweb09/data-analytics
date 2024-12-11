import numpy as np

# shape  --> gives the order of the matrix
arr:np.ndarray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

o:tuple = np.shape(arr)
# or
arr.shape
# print(o)  # returns a tuple of (rows, column)

# reshape
a = np.reshape(arr, [4,3])
print(a)

# size --> total no of elements
s:int = np.size(arr)

# ndim --> no of dimensions
d:int = np.ndim(arr)

# len --> no of nested elements
d:int = len(arr)

# dtype --> which datatype is used in the matrix
dt = arr.dtype
# print(dt)

# astype --> converting the datatype
# if i convert float to int, it will move to LOWER integer
at = arr.astype(float)
# print(at)
