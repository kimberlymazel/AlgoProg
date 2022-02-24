'''

Are there differences in activity patterns between weekdays and weekends?

1. Create a new factor variable in the dataset with two levels - "weekday" and "weekend" indicating whether a given
date is a weekday or weekend day.

2. Make a plot containing a time series plot of the 5-minute interval (x-axis) and the average number of steps taken,
averaged across all weekdays or weekend days (y-axis).

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = pd.read_csv("activity.csv")

file["steps"] = file["steps"].fillna(0)  # changing NaN to 0 in steps column
file["date"] = pd.to_datetime(file["date"])  # converts date column to datetime format

# adds a new column with number representing day of week
# 0: Monday, 7: Sunday
file["number"] = file["date"].dt.dayofweek

# numpy.where(condition, x, y)
# if condition met, it is weekend, if not, it is weekday (greater than 5 --> 6 and 7 = Sat/Sun)
# new column (type) to show if it is a weekend or weekday
file["type"] = np.where(file["number"] > 5, "weekend", "weekday")

# finds mean of steps by group of interval and type
grp = file.groupby(['interval', 'type'])['steps'].mean()

# resets index first and then sets it to interval for x value and steps for y value
# type for columns as they will have an individual subplot
pd.pivot_table(file.reset_index(), index='interval', columns='type', values='steps').plot(subplots=True)
plt.show()
