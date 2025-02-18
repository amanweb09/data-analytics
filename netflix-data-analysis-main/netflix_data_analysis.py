# -*- coding: utf-8 -*-
"""Netflix_Data_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y5V3yy-Rf_tUu0GY7mdVUqsnMelNlGwd
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("file.csv")
data.head()

"""**Handling null and duplicate values**"""

data.isnull().sum()

# looking at the duplicated values
data[data.duplicated()]

data = data.drop_duplicates()

# handling null values

data.isnull().sum()
# data.isna().sum()
data.dropna(inplace=True)

# heatmap of null values
ax = sns.heatmap(data=data.isnull())
plt.title("Null Values in the Dataset")

ax.set(xlabel = "Columns", ylabel = "Number of null values")
plt.show()

"""Ques. For "House of Cards", who is the director and what is the show ID?"""

# method 1
data[data["Title"] == "House of Cards"][["Show_Id", "Director"]]

# method 2
data[data["Title"].str.contains("House of Cards")]

"""Ques. In which year was the maximum number of TV Shows and movies were released? Show using bar graph"""

data["Release_Date_dt"] = pd.to_datetime(data["Release_Date"])

fig = plt.figure(figsize=(10, 6))
ax = sns.barplot(x=data["Release_Date_dt"].dt.year,
                 y=data["Release_Date_dt"].dt.year.value_counts(),
                 color="r", width=0.5, saturation=0.65)

fig.add_subplot(ax)
plt.title("Release Years of Shows and Movies")
ax.set(xlabel = "Years", ylabel = "Number of Movies Released")

plt.show()

"""How many movie and TV shows are there? Show with a bar graph"""

grouped_data = data.groupby(["Category"])
grouped_data["Category"].count()

ax = sns.barplot(data=grouped_data["Category"].count(), color="r")
plt.title("Number of TV Shows and Movies")

ax.set(xlabel="Category", ylabel="Number of Movies/Shows")
plt.show()

# or using the countplot
ax = sns.countplot(data["Category"], color="r")

plt.title("Number of TV Shows and Movies")
ax.set(xlabel="Category", ylabel="Number of Movies/Shows")
plt.show()

"""Ques: Show all the movies released in 2020


"""

data["Year_of_Release"] = data["Release_Date_dt"].dt.year
data[(data["Category"] == "Movie")&(data["Year_of_Release"] == 2020.0)]

"""Ques: Show title of all the movies released in India"""

data[(data["Category"] == "Movie")&(data["Country"] == "India")][["Title"]]

"""Ques: Show top 10 directors who gave max TV Shows and Movies to Netflix"""

data["Director"].value_counts()[:10]

"""Ques: All the records with comedy movies or country is UK"""

data[(data["Type"]=="Comedies")&(data["Category"]== "Movie") | (data["Country"] == "United Kingdom")]

"""Ques: All the movies and shows where Tom Cruise was casted"""

data[data["Cast"].str.contains("Tom Cruise")]

"""Ques: What are the different ratings defined by Netflix"""

data["Rating"].unique()

"""Ques: How many movies got TV-14 rating in Canada"""

movies = data[(data["Category"] == "Movie")&(data["Rating"] == "TV-14")&(data["Country"] == "Canada")]
number = movies.shape[0]

number

"""Ques: Maximum duration of a show/movie"""

data[["Minutes", "Units"]] = data["Duration"].str.split(" ", expand=True)
data["Minutes"].max()

"""Ques: The Country with maximum TV Shows"""

tv_shows = data[data["Category"]=="TV Show"]

tv_shows["Country"].value_counts().head(1)

"""Ques: Sort the dataset by year"""

data.sort_values(by="Year_of_Release", ascending=False)