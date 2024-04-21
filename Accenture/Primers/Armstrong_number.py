"""
Objective:

To work with Control structures

Problem Description:

If the sum of the cubes of  the digits in a three-digit number is equal to the number itself, then the number is called an Armstrong number.
E.g.: 153 is an Armstrong number because (13)+(53)+(33) = 153.
Write a program in Python to display all the  Armstrong numbers between n1 and n2.

Guidelines:

If the starting and ending numbers are negative then display the message "Starting and ending numbers must be greater than or equal to zero" and stop the program. 
If the starting number is greater than the ending number, then display the message "Invalid input!! Ending number should be greater than starting number" and stop the program. 
Refer to the sample input and output statements for more clarifications.
To get multiple input values in a single input(), use the below mentioned approach:
 n1,n2=map(int,input("Enter the starting and ending numbers:\n").split(" "))


Sample Input 1:

Enter the starting and ending numbers:

5 500

Sample Output 1:

Armstrong numbers between 5 and 500 are:

153

370

371

407

 

Sample Input 2:

Enter the starting and ending numbers:

50 100

Sample Output 2:

Armstrong numbers between 50 and 100 are:

There is no Armstrong number between these numbers

 

Sample Input 3:

Enter the starting and ending numbers:

1 10

Sample Output 3:

Armstrong numbers between 1 and 10 are:

1

 

Sample Input 4:

Enter the starting and ending numbers:

-4 2

Sample Output 4:

Starting and ending numbers must be greater than or equal to zero

 

Sample Input 5:

Enter the starting and ending numbers:

100 6

Sample Output 5:

Invalid input!! Ending number should be greater than starting number
"""

l = [int(x) for x in input("Enter the starting and ending numbers:\n").split()]
if l[0]<0 or l[1]<0:
    print("Starting and ending numbers must be greater than or equal to zero")
else:
    if l[0]>l[1]:
        print("Invalid input!! Ending number should be greater than starting number")
    else:
        num1, num2 = l[0], l[1]
        arm_numbers = []
        for i in range(num1, num2+1):
            sum_of_cubes = 0
            for j in str(i):
                sum_of_cubes+=(int(j)**3)
            if sum_of_cubes==i:
                arm_numbers.append(i)
        if arm_numbers:
            print(f"Armstrong numbers between {num1} and {num2} are:")
            for i in arm_numbers:
                print(i)
        else:
            print(f"Armstrong numbers between {num1} and {num2} are:")
            print("There is no Armstrong number between these numbers")
