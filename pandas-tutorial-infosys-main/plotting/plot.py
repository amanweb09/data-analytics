import pandas as pd

url = "http://bit.ly/imdbratings"

data = pd.read_csv(url, nrows=5)

p = data.duration.plot(kind="hist")
print(p)
