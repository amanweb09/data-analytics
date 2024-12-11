import numpy as np

# WHERE()

arr: np.ndarray = np.array([12, 55, 75, 6])

find_55_in_arr: tuple = np.where(arr == 55)
print(find_55_in_arr)   #returns index of 55 as tuple of array
# thus, index of 55 = find_55_in_arr[0][0]

# find all elements div by 2
div_by_2: tuple = np.where(arr % 2 == 0)
