import pandas as pd

# checking version
version = pd.__version__


data = pd.read_table(
    "https://bit.ly/movieusers",
    sep="|",
    header=None,
    names=["id", "Age", "gender", "occupation", "revenue"],
)

# describe -> gives data like mean, count, quartiles, etc (only for numerical values)
desc = data.describe()

# description for string values -> like max occuring values, count, etc
desc_str = data.describe(include="object")

# datatypes of series
dt = data.dtypes
