import pandas as pd

data_url = "https://bit.ly/imdbratings"
data = pd.read_table(data_url, sep=",")

# creating a new column
data["my_column"] = "Hello"

# updating
# inplace specifies if you want to retain the change
updates_dataframe = data.rename(columns={"star_rating": "stars"}, inplace=True)

# method 2
uppercase_columns = [s.capitalize() for s in data.columns]
data.columns = uppercase_columns

# method 3 - replacing _ with space
data.columns.str.replace("_", " ")

