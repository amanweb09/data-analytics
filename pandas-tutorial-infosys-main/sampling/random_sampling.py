import pandas as pd

data = pd.read_csv("http://bit.ly/drinksbycountry")

"""
Random sampling means getting any n random rows from the data
"""

# returns 10 random rows
sample = data.sample(n=10)
print(sample)


# returns same n values everytime
# same random state returns same random values everytime
sample = data.sample(n=6, random_state=45)


# return a fraction of data
sample = data.sample(frac=0.1)  # return 10 percent of the data
