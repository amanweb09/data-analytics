import pandas as pd

# this data has a lot of null values
url = "http://bit.ly/uforesports"
data = pd.read_csv(url, nrows=10)


# checking null
is_null = data.isnull()
not_null = data.notnull()


# checking missing values
is_na = data.isna()
not_na = data.notna()
