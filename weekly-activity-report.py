import csv
import numpy as np
from matplotlib import pyplot as plt 
import os 

# Get Data from CSV File and Load into Vectors 



#Convert Data to Hourly Average 
day1 = [1] * 144
day2 = [1] * 144
day3 = [1] * 144
day4 = [1] * 144
day5 = [1] * 144
day6 = [1] * 144
day7 = [1] * 144

week = [day1, day2, day3, day4, day5, day6, day7]

sum = 0
for day in week:

	for i in range(24):

		for x in range(1, 7):
			sum = sum + day[(6 * (i+1)) - x]

		day[i] = (sum/6) * 100
		sum = 0

day1 = day1[0:24]
day2 = day2[0:24]
day3 = day3[0:24]
day4 = day4[0:24]
day5 = day5[0:24]
day6 = day6[0:24]
day7 = day7[0:24]

#Create Graph
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
time = ['12 AM', '1 AM', '2 AM', '3 AM', '4 AM', '5AM', '6 AM','7 AM', '8 AM',
		'9 AM', '10 AM', '11 AM', '12 PM','1 PM', '2 PM', '3 PM', '4 PM', '5 PM',
		'6 PM', '7 PM', '8 PM', '9 PM', '10 PM', '11 PM']
ypos = np.arange(len(days))
plt.xticks(ypos, days)
plt.xlabel('Day of Week')
plt.ylabel('Percent Activity')
activity = np.empty(7, dtype=object)

mypath = 'graphs'
if not os.path.isdir(mypath):
	os.makedirs('graphs')

for j in range(24):
	for i in range(7):
		activity[i] = week[i][j]
	plt.title(time[j])
	plt.plot(ypos,activity)
	plt.savefig('graphs/' + time[j])
