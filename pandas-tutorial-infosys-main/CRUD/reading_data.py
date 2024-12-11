import pandas as pd

# read_table --> reads .dbs data
# we are using .dbs file (data is separated by Tab)
# data is identified by (row label, column label)

# reading tables
reading_tables_or_dsb = pd.read_table("https://bit.ly/chiporders")

# reading csv
reading_csv = pd.read_csv("http://bit.ly/imdbratings")
# OR (as csv data is comma separated)
reading_csv = pd.read_table("http://bit.ly/imdbratings", sep=",")


# if data is separated by a character (eg. comma, pipe, space, etc)
# sep indicates the separator
# header indicates that table has no headers
# names indicate the headers of the columns
data_url = "https://bit.ly/movieusers"
column_names = ["id", "Age", "gender", "occupation", "revenue"]

data = pd.read_table(data_url, sep="|", header=None, names=column_names)

data.head() # printing from start (default: 1st 5 rows)

data.tail() # printing from end (default: last 5 rows)

data.columns    #printing the column names

data.shape #(rows, cols)
