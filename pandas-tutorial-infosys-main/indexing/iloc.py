import pandas as pd

"""
set country as the index column 
"""
drinks = pd.read_csv("http://bit.ly/drinksbycountry", nrows=10, index_col="country")

"""
iloc
helps in selecting data by position
"""

# 3rd row and 2nd column
alg_wine = drinks.iloc[3, 2]
