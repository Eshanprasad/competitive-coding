"""
Objective: 

To work with array sorting

 

Problem Description: 

You are developing a weather monitoring application for a city. The application requires the user to enter the temperature records for a specified number of days. Once the temperature records are entered, the application will perform the following tasks:

Calculate the mean temperature for the specified days.
Identify the day with the highest temperature and display its corresponding day number with temperature.
Identify the day with the lowest temperature and display its corresponding day number with temperature.
Sort the days based on temperature in ascending order and display the corresponding day numbers with temperature.
 

Process flow:

Get the number of days and temperature records for each day from the user as input.
Create an array based on number of days and calculate the mean temperature, which day has the highest and lowest temperature, and sort the days based on temperature in ascending order.
Display the details as per the sample output statement.
 Note:

Create an array and store each day's temperature  in a variable named ''temperatures"
Display the mean temperature in 2 decimal place


Sample Input 1:

Enter the number of days: 5

Enter temperature records for 5 days:

Day 1: 35.5

Day 2: 34.3

Day 3: 36.1

Day 4: 35.4

Day 5: 33.2

 

Sample Output 1:

Temperature Records for the City:

[35.5 34.3 36.1 35.4 33.2]

 

Mean Temperature for 5 Days: 34.90

Day with the Highest Temperature: Day 3 Temperature: 36.1

Day with the Lowest Temperature: Day 5 Temperature: 33.2

 

Days Sorted by Temperature (Ascending Order):

Day 5: Temperature 33.2

Day 2: Temperature 34.3

Day 4: Temperature 35.4

Day 1: Temperature 35.5

Day 3: Temperature 36.1
"""


import numpy as np

days=int(input('Enter the number of days: \n'))
records=[]
print(f'Enter temperature records for {days} days:')
for i in range(1,days+1):
    temp=float(input(f'Day {i}: \n'))
    records.append(temp)
temperatures=np.array(records)
print(f'Temperature Records for the City:\n{temperatures}')
print(f'\nMean Temperature for {days} Days: {np.mean(temperatures):.2f}')
max_temp,max_day=np.max(temperatures),np.argmax(temperatures)+1
min_temp,min_day=np.min(temperatures),np.argmin(temperatures)+1
print(f'Day with the Highest Temperature: Day {max_day} Temperature: {max_temp}')
print(f'Day with the Lowest Temperature: Day {min_day} Temperature: {min_temp}')
sorted_index=np.argsort(records)
sorted_days=sorted_index+1
print(f'\nDays Sorted by Temperature (Ascending Order):')
for i in range(days):
    print(f'Day {sorted_days[i]}: Temperature {temperatures[sorted_index[i]]}')
