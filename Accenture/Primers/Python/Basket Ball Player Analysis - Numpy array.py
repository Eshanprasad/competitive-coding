"""
Objective: 

To work with Array slicing

 

Problem Description: 

In a thrilling basketball game, Team A and Team B competed fiercely. The coach of Team A wants to analyse the performance of their star player, John, throughout the game. John's points for each quarter are recorded in an array.

In a game, there are 4 quarters and John scores points in each quarter. The coach wants to analyse the total points scored by John in the first two quarters and find the average point he scored in the final quarter. Help his coach to analyse the John points using a Numpy array in Python.

Process flow:

Get the four points in each quarter he has scored as user input.
Store all the scores in a 4*4 array.
Find the total points of the first two quarters he scored and also find the average points of the last quarter he scored.
Display the details a per the sample input and output statement
 Note:

The input should be a integer value
Create an array and store the value of all quarter points of John's  in the variable named ''john_statistics".
Display the total points and average points should be in 2 decimal places


Sample Input Statement:

Enter John's points for each quarter:

Quarter 1, Point 1: 4

Quarter 1, Point 2: 5

Quarter 1, Point 3: 6

Quarter 1, Point 4: 2

Quarter 2, Point 1: 3

Quarter 2, Point 2: 4

Quarter 2, Point 3: 2

Quarter 2, Point 4: 6

Quarter 3, Point 1: 7

Quarter 3, Point 2: 1

Quarter 3, Point 3: 3

Quarter 3, Point 4: 6

Quarter 4, Point 1: 2

Quarter 4, Point 2: 6

Quarter 4, Point 3: 3

Quarter 4, Point 4: 7

 

Sample Output Statement:

 

John's Statistics:

[[4 5 6 2]

 [3 4 2 6]

 [7 1 3 6]

 [2 6 3 7]]

 

Total points scored by John in the first 2 quarters : 32.00

Average points scored by John in the last quarter: 4.50
"""

import numpy as np

points=[]
print("Enter John's points for each quarter:")
for i in range(1,5):
    for j in range(1,5):
        point=int(input(f'Quarter {i}, Point {j}:\n'))
        points.append(point)
john_statistics=np.array(points).reshape(4,4)
print("John's Statistics:")
print(john_statistics)
total_points=np.sum(john_statistics[:2])
average_points=np.mean(john_statistics[-1])
print('\nTotal points scored by John in the first 2 quarters : {:.2f}'.format(total_points))
print('Average points scored by John in the last quarter: {:.2f}'.format(average_points))
