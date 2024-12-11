import pandas as pd

url = "http://bit.ly/imdbratings"
data = pd.read_csv(url, nrows=5)

# resets the index to row labels
# inplace means to make it permanent
data.reset_index(inplace=True)
