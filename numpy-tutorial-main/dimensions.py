import numpy as np

# Adding dimensions in an array
# np.array(d1, d2,...)

# 1d array
a_1d: np.ndarray = np.array([10, 20, 30])

# 2d
# all the dimensions must have same number of elements
a_2d: np.ndarray = np.array([[10, 20, 30], [1, 2, 3]])
print(a_2d)
