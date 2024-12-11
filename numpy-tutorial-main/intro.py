import numpy as np

# creating an array
# np.array(LIST)
a1: np.ndarray = np.array([10, 20, 30])
a2: np.ndarray = np.array([2, 3, 4])

# creates array with 1 row 5 columns with elements as 1
b: np.ndarray = np.ones(5)  # elements will be float
b1: np.ndarray = np.ones(5, dtype=int)  # elements will be int

# create 2d
c: np.ndarray = np.ones([3,3], dtype=int)

# create zero matrix
z: np.ndarray = np.zeros([3, 3], dtype=int)

# creating array through a range
d = np.arange(3)    #creates an array from 0 to 2 (3 is excluded)
# or
d = np.array(range(0, 3))
# or
d = np.arange(15, 0, -1)    #just like range

# precendence
# string > int, float > int
# if one element is a string and rest are int, all the elements will be converted to string

a3: np.ndarray = np.array([7, 8, "9"])

# accessing columns
a1[:, 0]  # slice all and return the 1st column

# height, weight
players = [(170, 63), (180, 70), (185, 60), (200, 95), (160, 50)]
skills = ["bat", "bat", "wk", "bowler", "AR"]

# what is the height of person who is at 2nd index
h = players[2][0]

# all the players who are batsmen
s = players[skills == "bat"]
