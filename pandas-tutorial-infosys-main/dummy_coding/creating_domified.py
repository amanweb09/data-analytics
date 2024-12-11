import pandas as pd

titanic = pd.read_csv("http://bit.ly/kaggletrain", nrows=10)

# dummify sex and embarked columns of titanic
# it gets auto prefixed  ==> Sex_male, Sex_Female
dummy = pd.get_dummies(titanic, columns=["Sex", "Embarked"])

# Drop_first -> returns only n-1 of n categories
# eg. if one category is female, other is obv male, so no need of male column
dummy = pd.get_dummies(titanic, columns=["Sex", "Embarked"], drop_first=True)
