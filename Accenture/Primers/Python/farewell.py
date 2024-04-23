'''
Objective:

To work with Functions and modules

Problem Description:

Tom studies at a boys' college and his team at college are planning to organize a farewell party for their seniors.  Tom wants to develop an application to generate a welcome message to each senior on the screen when they enter the senior's name.   Help Tom to perform this task by creating a module in Python.   
Note:

1. Create a module called "greet.py" which contains :

A message variable that contains the message "Hello"
 A function 'greet(name)' should take a string as the parameter and should print that name along with a greeting message.
A documentation string: """ Module for Greeting"""

2. Call this documentation string, functions, and message variable by importing the greet module. 

3. Refer to the sample input and output statements for more details.


Sample Input 1:

Enter the senior's name: James



Sample Output 1:

Hello Mr.James, Welcome to the farewell Party!!!  

Documentation string: Module for Greeting

'''


# farewell.py
import greet
name=input("Enter the senior's name: ")
print(greet.message,end=' ')
greet.greet(name)
print('Documentation string:',greet.greet.__doc__)


# greet.py
def greet(name):
    """Module for Greeting"""
    print(f"MR.{name}, Welcome to the farewell Party!!!")
    
message = "Hello"
