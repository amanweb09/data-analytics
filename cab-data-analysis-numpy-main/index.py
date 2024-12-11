import numpy as np

taxi: np.ndarray = np.genfromtxt("nyc_taxis.csv", delimiter=",", skip_header=True)

# Q1. find the mean speed of all the rides

speed: np.ndarray = taxi[:, 7] / (taxi[:, 8] / 3600)
mean_speed: float = np.mean(speed)

print(mean_speed)


# Q2. FInd the number of rides in Feburary
taxi_filter: bool = taxi[:, 1] == 2  # 2nd column == feb
rides_in_feb: np.ndarray = taxi[taxi_filter]
number_in_feb: int = np.shape(rides_in_feb)[0]

print(number_in_feb)


# Q3. Number of rides with tip > USD 50
tip_filter: bool = taxi[:, -3] > 50  # 3rd col from the last > 50 USD
rides: np.ndarray = taxi[tip_filter]
number_with_tip_50: int = np.shape(rides)[0]

print(number_with_tip_50)
