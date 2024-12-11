import pandas as pd

movie_data = "http://bit.ly/imdbratings"
data = pd.read_csv(movie_data, nrows=5)

# 1. Using for loop
# data.title is a series and series is an iterable
for title in data.title:
    print(title)


# using iterrow function
for i, row in data.iterrows():
    print(row.title)
