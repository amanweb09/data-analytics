import numpy as np

# concatenate

a1:np.ndarray = np.array([1,2,3])
a2:np.ndarray = np.array([4,5,6])

# concatenates [...a1...a2]
con:np.ndarray = np.concatenate([a1, a2])

a3:np.ndarray = np.array([[1,2,3], [11,22,33]])
a4:np.ndarray = np.array([[4, 5, 6], [44, 55, 66]])

# [[A1], [A2], [B1], [B2]]
# default axis is 0
con_horiz:np.ndarray = np.concatenate([a3, a4])

# concatenate column wise i.e. both 1d arrays conc together and 2d get together
# [[A1 B1], [A2 B2]]
con_vertically:np.ndarray = np.concatenate([a3, a4], axis=1)
print(con_vertically)

# ---------------------------------
# concat using hstack and vstack
np.hstack([a3,a4])  #horizontal concat  
np.vstack([a3, a4])
