import pandas as pd

movie_data = "http://bit.ly/imdbratings"
data = pd.read_csv(movie_data, nrows=15)

# ques: group all crime movies together, romance together, and so on
grouped_data = data.groupby("genre")

# ques: find mean duration of each genre
md = grouped_data.duration.mean()

# find max, min, and median together
x = grouped_data.duration.agg(["min", "max", "median", "count"])
