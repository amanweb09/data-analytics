import pandas as pd


data = pd.DataFrame(
    {
        "Id": [1, 2, 3, 4, 1, 1, 2],
        "Name": ["aman", "goku", "gohan", "vegeta", "aman", "aman", "goku"],
    }
)

# duplicated method returns true if it occured before
x = data.Name.duplicated()
print(data[x])

# dropping duplicates
drop = data.drop_duplicates()
