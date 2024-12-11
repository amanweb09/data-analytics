import numpy as np
import statistics as stats

carbs = [100, 150, 200, 70, 180]
arr = np.array(carbs)

# mean
x:float = np.mean(arr)

# median
me:float = np.median(arr)

# mode
mo = stats.mode(arr)

# standard deviation
sd = np.std(arr)
print(sd)

# variance
v = np.var(arr)

# correlation
# +1 -> strong positive relation
# -1 -> strong inverse relation
tobacco = np.array([10, 15, 30, 60])
death = np.array([100, 200, 500, 1000])

co:float = np.corrcoef(tobacco, death)