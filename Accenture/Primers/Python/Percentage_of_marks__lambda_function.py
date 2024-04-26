"""
Objective:

To work with Functions

Problem Description:

Accept 3 subject marks from the user and pass them to the lambda function which will return the percentage of the total marks. Display the percentage on the console.
Guidelines:

Get 3 marks from the user and store into the variables 'subject1', 'subject2' and 'subject3' respectively.  Each mark should be out of 100.

Create the lambda function which should return the percentage of total marks and assign to the variable named: 'cal'

Strictly follow the naming conventions for variables and functions as specified in the problem description.

Sample Input and Output:

Enter marks for subject1: 50

Enter marks for subject2: 23

Enter marks for subject3: 59

Percentage is 44.0
"""

subject1= int(input("Enter marks for subject1: "))
subject2= int(input("Enter marks for subject2: "))
subject3= int(input("Enter marks for subject3: "))
cal = lambda subject1, subject2, subject3: ((subject1+subject2+subject3)/300)*100
print(f"Percentage is {cal(subject1, subject2, subject3)}")
