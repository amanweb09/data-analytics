import pandas as pd

data_url = "https://bit.ly/imdbratings"
data = pd.read_table(data_url, sep=",")

filter_ = [True if duration >= 175 else False for duration in data.duration]

# it will now show only the data which has True
filtered_movies = data[filter_]

# or
filtered_movies = data[data.duration >= 175]