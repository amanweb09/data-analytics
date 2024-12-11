import numpy as np

a1: np.ndarray = np.array([1, 2, 3, 4, 5])
a12: np.ndarray = np.array([[1, 2, 3], [100, 200, 300]])

# adding
a2: np.ndarray = np.append(a1, 100)
# 2d gets converted into 1d
a21: np.ndarray = np.append(a12, [[100], [785]])


# IMP: adding to different dims
a22: np.ndarray = np.append(a12, [[100], [785]], axis=1)


# adding on a specific index
# arr, index, value
a3: np.ndarray = np.insert(a1, 2, 150)

# IMP: inserting in 2d array
a4: np.ndarray = np.insert(a12, 2, [150,125], axis=1)

# deleting value
# arr, index
a5: np.ndarray = np.delete(a1, 2)
