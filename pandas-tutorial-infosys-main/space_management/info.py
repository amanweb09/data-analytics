import pandas as pd

data = pd.read_csv("http://bit.ly/imdbratings", nrows=5)

# info shows details like memory usage, dtypes, etc
# deep means show the actual uasge and not just the amount of data in bytes
info = data.info(memory_usage="deep")
print(info)


# memory usage only by each series
mem = data.memory_usage(deep=True)
print(mem)
