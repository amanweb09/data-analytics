import numpy as np

# create an array
arr: np.ndarray = np.array([54, 45, 85, 22])

# create a filter
# True for the values that I want and False for not
fil = [True, False, True, False]

filtered_arr = arr[fil]
print(filtered_arr)

# ----------- Method 2
filtered_arr = arr[arr < 30]
print(filtered_arr)

