import pandas as pd

data_url = "https://bit.ly/imdbratings"
data = pd.read_table(data_url, sep=",")

# sort in ascending order
sorted_data = data["duration"].sort_values()
# OR
sorted_data = data.sort_values("duration")

# descending
# data["duration"].sort_values(ascending=False)

# multiple fields
sorted_data = data.sort_values(["duration", "genre"])
