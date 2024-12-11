import pandas as pd

url = "http://bit.ly/imdbratings"

data = pd.read_csv(url, nrows=5)

# description
desc = data.genre.describe()

# ques: find which is the most popular genre
most_pop = desc.top
print(f"{most_pop} occurs {desc.freq} times")


# ques: find how many times each genre occurs
count_genre = data.genre.value_counts(""" normalize=True for percentages """)


# ques: find all the unqiue genres
unique_genres = data.genres.unique()  # returns an array
