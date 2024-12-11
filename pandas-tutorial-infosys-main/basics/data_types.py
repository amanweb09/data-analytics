"""
1. SERIES
    Columns of the data are called series eg. name, age, gender
    All the elements of a series must of the same datatype

2. DATAFRAME
    The data which are talking about
    A collection of series is called a dataframe

"""

import pandas as pd

movie_data = "http://bit.ly/imdbratings"
data = pd.read_csv(movie_data)

dt = data.dtypes
