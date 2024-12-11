import pandas as pd

movie_data = "http://bit.ly/imdbratings"
data = pd.read_csv(movie_data, nrows=5)

# we always use STR method for manipulating series

# uppercase
uc = data.title.str.upper()

# all the titles that contain a particular word
cont = data.title.str.contains("The")

# replacing a substring
rep = data.title.str.replace("The", "A")
