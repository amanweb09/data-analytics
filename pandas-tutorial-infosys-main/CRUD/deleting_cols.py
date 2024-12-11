import pandas as pd

data_url = "https://bit.ly/imdbratings"
data = pd.read_table(data_url, sep=",")

# Drop 
"""
Axis
1 --> vertical (columns)
0 --> horizontal (rows)
"""
# axis = 1 specify delete a column
data.drop("genre", axis=1, inplace=True)

