"""
Objective:

To work with Functions and 



Problem Description:

The environmental Eco club at Coimbatore has discovered a new amoeba that grows in the order of Fibonacci series every month, up to 12 months. They are exhibiting their amoeba in a national conference. They want to know the size of the amoeba at a particular instance. Given a month's index, can you write a  Python program that displays the amoeba's size on that month using a user defined function ? 
 
Note:
The size of the amoeba on months 1, 2, 3, 4, 5, 6, .. will be 0, 1, 1, 2, 3, 5, 8 respectively.
Function format should be: fibonacci(number) and it should return the size of amoeba.
The numeric input value for the month should be between 1-12.  Else display the message "Invalid month".
Refer the sample input and output for more clarifications.


Sample Input 1:
Enter the month as numeric value:
7

Sample Output 1:
The amoeba size is 8
 
Sample Input 2:
Enter the month as numeric value:
12

Sample Output 2:
The amoeba size is 89

Sample Input 3:
Enter the month as numeric value:
0

Sample Output 3:
Invalid month



Sample Input 4:
Enter the month as numeric value:
13

Sample Output 4:
Invalid month
"""




def fibonacci(number):
    l = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    return l[number-1]

month = int(input("Enter the month as numeric value:\n"))
if month<=0 or month>12:
    print("Invalid month")
else:
    print(f"The amoeba size is {fibonacci(month)}")
