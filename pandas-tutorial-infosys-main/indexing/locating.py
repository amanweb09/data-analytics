import pandas as pd

url = "http://bit.ly/imdbratings"
data = pd.read_csv(url, nrows=5)

# loc[row, column]
# 0th row and all columns
data.loc[0, :]

# 3 rows and all columns
x = data.loc[[0, 1, 2], :]


# selecting through range
# IMP: both 0 and 2 are included
y = data.loc[0:2, :]

# selecting whole data
z = data.loc[:, :]

# ques: select all the rows of genre
genres = data.loc[:, "genre"]
print(genres)

# ques: select all rows where genre is not action
not_action = data.loc[data.genre != "action", :]

# ques: select all rows of genre and title
g_t = data.loc[:, ["genre", "title"]]
print(g_t)
