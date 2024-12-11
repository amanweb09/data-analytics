import pandas as pd


data_url = "https://bit.ly/movieusers"
column_names = ["id", "Age", "gender", "occupation", "revenue"]

data = pd.read_table(data_url, sep="|", header=None, names=column_names)

# Dataframe[Series_Name]
age = data["Age"]
# or
age = data.Age


# ---------- selecting a particular field => USECOLS
movie_data = "http://bit.ly/imdbratings"
data = pd.read_csv(movie_data, usecols=["title", "genre"])


# ------- reading only n rows
data = pd.read_csv(movie_data, nrows=5)
print(data)
