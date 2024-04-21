"""
Objective:

To work with Control structures

Problem Description:

The Factorial of any number n is represented by n! which is equal to 1*2*3*....*(n-1)*n.

E.g.:
4! = 1*2*3*4 = 24
3! = 3*2*1 = 6
2! = 2*1 = 2
Also,
1! = 1
0! = 1


Write a Python program to calculate the factorial of any given number.  If you enter a negative number, display "Factorial does not exist for negative numbers" and stop the program. 



Sample Input 1:
Enter a number

5

Sample Output 1:

Factorial is 120

 

Sample Input 2:

Enter a number

0

Sample Output 2:

Factorial is 1

 

Sample Input 3:

Enter a number

-5

Sample Output 3:

Factorial does not exist for negative numbers
"""

number = int(input("Enter a number\n"))
if number<0:
    print("Factorial does not exist for negative numbers")
else:
    if number==0:
        print("Factorial is 1")
    else:
        prod = 1
        for i in range(number, 0, -1):
            prod*=i
        print("Factorial is", prod)
