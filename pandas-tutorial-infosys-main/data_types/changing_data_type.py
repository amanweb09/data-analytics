import pandas as pd

movie_data = "http://bit.ly/imdbratings"
data = pd.read_csv(movie_data, nrows=5)

# changing the data after importing
data.duration = data.duration.astype("float")

# changing the data while importing
data = pd.read_csv(movie_data, nrows=5, dtype={"duration": float})

# Ques: we are given order value in USD and we need to take the mean
# sol: remove dollar sign and convert into a float

orders = pd.read_table("http://bit.ly/chiporders", nrows=5)

x = orders.item_price.str.replace("$", "").astype("float")
print(x.mean())


# Ques: check if a movie title has "and" in it and convert boolean to integer (0 and 1)
if_and = data.title.str.contains("and").astype("int")
