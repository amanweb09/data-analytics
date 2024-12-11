import numpy as np

arr1: np.ndarray = np.array([[1, 2, 3], [5, 6, 7]])
arr2: np.ndarray = np.array([[100, 200, 300], [500, 600, 700]])


# addition
add: np.ndarray = arr1 + arr2
add: np.ndarray = np.add(arr1, arr2)

# subtract
diff:np.ndarray = arr1 - arr2
diff:np.ndarray = np.subtract(arr1, arr2)

# same for divide() and multiply()

# power
# all the elements will be cubed
a3:np.ndarray = np.array([3])
print(np.power(arr1, a3))

# 1st dimensions raised to power 3, 2nd to the power 2
a4:np.ndarray = np.array([[3], [4]])
print(np.power(arr1, a4))

a5:np.ndarray = np.array([2,3])
# print(np.power(arr1, a5))  ERROR
