import csv
import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt

#Get Data from CSV file and Load into a Vector 



#Plot Data 
data = [1] * 144
activity = np.empty(24, dtype=object)
sum = 0
i = 1
j = 0

for point in data:
	
	try:
		sum = sum + int(point)
	except: 
		continue
	
	if (i == 0):
		i = i + 1
		continue

	if (i%6 == 0):
		activity[j] = (sum/6) * 100 
		sum = 0
		j = j + 1

	i = i + 1

time = ['12 AM', '1 AM', '2 AM', '3 AM', '4 AM', '5AM', '6 AM','7 AM', '8 AM',
		'9 AM', '10 AM', '11 AM', '12 PM','1 PM', '2 PM', '3 PM', '4 PM', '5 PM',
		'6 PM', '7 PM', '8 PM', '9 PM', '10 PM', '11 PM']

ypos = np.arange(len(time))
plt.xticks(ypos, time)
plt.xlabel('Hour of Day')
plt.ylabel('Percent Activity')
plt.title('Activity Index for Room')
plt.bar(ypos, activity)
plt.show()














