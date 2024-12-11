import pandas as pd

url = "http://bit.ly/imdbratings"
data = pd.read_csv(url, nrows=25)

# creates a table with genre as rows and corresponding rating as columns
table = pd.crosstab(data.genre, data.content_rating)
print(table)
