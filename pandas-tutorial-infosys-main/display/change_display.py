import pandas as pd

"""
Pandas by default shows 1st 30 rows then ... then last 30 rows
i.e. total 60 rows

We can change it by using get_option() and set_option()
"""

drinks = pd.read_csv("http://bit.ly/drinksbycountry")

# ques: count total number of rows displayed
total_rows = pd.get_option("display.max_rows")

# changing max rows
pd.set_option("display.max_rows", 100)

# no limit
pd.set_option("display.max_rows", None)

# reseting the data
pd.reset_option("display.max_rows")
