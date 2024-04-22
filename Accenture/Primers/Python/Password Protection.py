"""
Objective:

To work with Lists

Problem Description:

The owner of a block layout has some plot numbers with odd numbers and some with even numbers. He is maintaining the details in a file in the system. For the password protection the owner has followed one formula. He calculated the sum of his even number plots and sum of odd number plots and found the average of those two and he used that average as his password for the file.   Write a Python program to arrive at the password for the file, by entering the plot numbers. 
 
Input and Output Format:
Input consists of n+ 1 numbers. The first number corresponds to n which is the number of plots. The next 'n' numbers correspond to the plot numbers and these plot numbers can be integers or floats.

The output consists of a floating point number that corresponds to the average. It is displayed with  2 decimal places.  Assume that the maximum number of plots should not be greater than 20.


Guidelines:

The size of the list should always be a positive number between 1 and 20. If not, display the message "Invalid Input" and terminate the program.
While entering list elements, make sure that you enter positive values only.   If not, it should print "Invalid Input" and terminate the program immediately.
Use list comprehension for finding odd and even numbers.
 
Sample Input 1:
Enter the total no.of plots: 5
Enter the numbers of each plot:
1
2
3
4
5

Sample Output 1:
The password for the file is: 7.50
 
Sample Input 2:
Enter the total no.of plots: -5

Sample Output 2:
Invalid Input
 
Sample Input 3:
Enter the total no.of plots: 5
Enter the numbers of each plot:
23
2
-5

Sample Output 3:
Invalid Input
 
Sample Input 4:
Enter the total no.of plots: 8
Enter the numbers of each plot:
10
90
5
0

Sample Output 4:
Invalid Input
 
Sample Input 5:
Enter the total no.of plots: 21

Sample Output 5:
Invalid Input
"""

total=int(input('Enter the total no.of plots:'))
if total<1 or total>20:
    print('Invalid Input')
    quit()
plots=[]
print('Enter the numbers of each plot:')
for i in range(total):
    plot=float(input())
    if plot<=0:
        print('Invalid Input')
        quit()
    plots.append(plot)
odd=sum([i for i in plots if i%2!=0])
even=sum([i for i in plots if i%2==0])
avg=(odd+even)/2
print(f'The password for the file is: {avg:.2f}')
