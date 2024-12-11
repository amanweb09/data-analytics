import pandas as pd

drinks = pd.read_csv("http://bit.ly/drinksbycountry", nrows=5)

"""
int and float occupy the least space
"""

"""
Space optimisation can be done best in case of categorical data
as rather than storing strings everytime we can store an int and create a table 
of which int is referring to which category

Here we do it with continents
"""

"""
category datatype auto creates a table and stores the categories as int
"""

# step 1 is to check how many unique values we have
print(drinks.continents.unique())

# convert to category dtype
drinks.continent = drinks.continent.astype("category")

# checking the int codes of each category
print(drinks.continent.cat.codes)
