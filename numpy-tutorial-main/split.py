import numpy as np

a1: np.ndarray = np.array([1, 2, 3, 4, 5, 6, 7])

# array, no of sub-arrays you want, axis=0
split_arr: np.ndarray = np.array_split(a1, 4)
# print(split_arr)

# split_array vs split
# In split_array, the sub-arrays can be of different length,
# while in split, the sub-arrays will be of equal length

# 2d array --> separates dimensions
a2: np.ndarray = np.array([[1, 2, 3], [5, 6, 7]])
split_dim: np.ndarray = np.array_split(a2, 2)   #separates the dimensions into 2 parts

# no of sub-arrays > dimensions => empty array
parts_more_than_dims: np.ndarray = np.array_split(a2, 4)
print(parts_more_than_dims)
