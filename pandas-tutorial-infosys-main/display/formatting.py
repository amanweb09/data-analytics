import pandas as pd

drinks = pd.read_csv("http://bit.ly/drinksbycountry", nrows=10)

# let's create a column with huge numbers
drinks["wine"] = drinks.wine_servings * 1e5

"""

formatting means using commas in numbers, changing width of columns

NOTE: Only floats can be formatted (not int)

"""

# formats to 1000
pd.set_option("display.float_format", "{:,}".format)

# changing column width
max_width = pd.get_option("display.max_colwidth")
pd.set_option("display.max_colwidth", 100)
