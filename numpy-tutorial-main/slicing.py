import numpy as np

# ****** FOR 1D Arrays
arr = np.array([2, 5, 78, 56])

# end value is not included
sliced_array = arr[0:3]

# start to end
sliced_array = arr[::]

# reverse
reversed_array = arr[::-1]

# ******* FOR 2D Arrays
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# arr[1st dim, 2nd dim]
# both the slices should have equal length as both the dimensions must have same no of elements
sliced_arr_2d = arr_2d[0:2, 0:2]
arr_2d[0:2, 0:3]    #still it will return 0:2

# slicing individual dimension
arr_2d[0, 1:2]  #arr[index of the array, slice]

