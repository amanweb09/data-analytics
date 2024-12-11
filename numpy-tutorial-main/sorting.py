import numpy as np

arr: np.ndarray = np.array([55, 14, 25, 3, 72])

# ascending order
sorted_arr: np.ndarray = np.sort(arr)

# 2d
arr_2d: np.ndarray = np.array([[55, 14, 25], [14, 2, 66]])

print(np.sort(arr_2d))
