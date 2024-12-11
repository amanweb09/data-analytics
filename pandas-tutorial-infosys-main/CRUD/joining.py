import pandas as pd

countries = pd.DataFrame(
    {
        "index": ["x", "y", "z"],
        "id": [i for i in range(0, 3)],
        "country": ["India", "Japan", "Germany"],
    }
)
countries = countries.set_index("index")

capitals = pd.DataFrame(
    {
        "index": ["y", "z"],
        "capitals": ["Tokyo", "Berlin"],
    }
)
capitals = capitals.set_index("index")

"""
if we join these 2 dataframes, there should be 1 common column or index
and the values will be assigned to corresponding indexes 

since there is no capital corresponsing to x index, it will show NaN in front of India 
"""

data = pd.concat([countries, capitals], axis=1)
print(data)
