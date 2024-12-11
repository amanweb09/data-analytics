import pandas as pd
import numpy as np

# from a dictionary
data = pd.DataFrame(
    {
        "Id": [1, 2, 3, 4],
        "Name": ["Aman", "Goku", "Gohan", "Vegeta"],
        "Skills": ["Pandas", "Web Dev", "Devops", "Power BI"],
    }
)


# from a list of lists
data_1 = pd.DataFrame(
    [
        [1, "aman"],
        [2, "goku"],
        [3, "gohan"],
    ]
)

# from a numpy array
# rand creates a 3x3 array with random values from 0-1
arr = np.random.rand(3, 3)
data_2 = pd.DataFrame(arr)


# using np for different rows
data_3 = pd.DataFrame(
    {
        "id": np.arange(1, 11),  # generates numbers from 1-10
        "grades": np.random.randint(0, 100, 10),  # generates 10 random integers
    }
)
