import pandas as pd

movie_data = "http://bit.ly/uforeports"
data = pd.read_csv(movie_data, nrows=15)

# converting to datetime
data.Time = pd.to_datetime(data.Time)

# dt is used for using datetime functions
hour = data.Time.dt.hour
minutes = data.Time.dt.minute

is_leap = data.Time.dt.is_leap_year
is_month_start = data.Time.dt.is_month_start


# conversion to date time
data = pd.DataFrame(
    {
        "day": [1, 11, 21],
        "month": [3, 9, 11],
        "year": [2022, 2023, 2024],
    }
)
dt = pd.to_datetime(data)
print(dt)
