"""
dummy coding means converting a categorical data into a numeric data
** We can also call it mapping
"""

import pandas as pd

titanic = pd.read_csv("http://bit.ly/kaggletrain", nrows=10)

# here true and false is rep with 1 and 0.. we will comvert it into true and false
# for this we create a map

# here we will rep male with 1 and female with 0
titanic["is_male"] = titanic.Sex.map(
    {
        "male": 1,
        "female": 0,
    }
)
# print(titanic.is_male)

# case 2: when categories are more
# we use get_dummies method to auto-assign integers to categories
dummies = pd.get_dummies(titanic["Embarked"])
print(dummies)

# concat the dummies along the rows
pd.concat([titanic, dummies], axis=0)
