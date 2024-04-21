"""
Objective:

To work with Lists

Problem Description:

Teachers of Indian Academy Public School collect the names of those students who are going to participate in the Mathematics exhibition, which is to be held in a week's time.  They have collected all the names and now, they want to store all the names in a system, in descending order of the length of the names.  This means the longest name should get stored first, followed by the name that is shorter than the previous one, and so on.    Can you help the teachers to perform this task easily by creating a program in Python?
Note:   The number of names specified must be positive, else the program should display the message "Invalid Input" and terminate the program.

Input format:

Input consists of an integer that corresponds to the number of names followed by the names

Output Format:

Print the name list sorted by the names' length, if name lengths are equal sort based on alphabetical order in descending order as shown in the sample input and output.

 

Sample Input and Output 1:

Enter the number of names:
5

Enter the names:
Safiq
Manish
Arun
Sanisha
Kumar

The sorted name list is:
Sanisha
Manish
Safiq
Kumar
Arun

Sample Input and Output 2:

Enter the number of names:
-1

Invalid Input



Sample Input and Output 3:

Enter the number of names :3
Enter the names:
Veena
Jeena
Meena

The sorted name list is:
Veena
Meena
Jeena
"""


num_of = int(input("Enter the number of names:\n"))
if num_of<=0:
    print("Invalid Input")
else:
    print()
    print("Enter the names:")
    l = []
    for i in range(num_of):
        l.append(input())
    l.sort(reverse=True)
    l.sort(key=len, reverse=True)
    print()
    print("The sorted name list is:")
    for i in l:
        print(i)
