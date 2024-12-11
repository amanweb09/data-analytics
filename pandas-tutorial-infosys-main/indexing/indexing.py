import pandas as pd

url = "http://bit.ly/imdbratings"
data = pd.read_csv(url, nrows=5)

# index = row labels (row number)

# setting a custom index
data.set_index("title")  # genre will act as an index now

# locating
# ques: find the genre of The Godfather
data.loc("The Godfather", "genre")  # here 1st argument is the index
