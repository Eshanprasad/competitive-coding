"""
Objective:

To work with Functions



Problem Description:

Sona, a Computer Science aspirant gets an assignment to write a program in Python to find out whether the given number is lucky or not by using a function.  A number is said to be lucky if the sum of the digits of that number is even. 
The function 'find_lucky()' accepts a numeric value and returns 0 or 1. If the return value is 1, then the number is lucky and if the return value is 0, the number is not lucky. Help Sona to write the code.

Note:

If the number is 0 or less, display the message "Invalid Number" and terminate the program.


Sample Input and Output 1:

Enter the Number:191

191 is not lucky



Sample Input and Output 2:

Enter the Number:123

123 is lucky


Sample Input and Output 3:

Enter the Number:0

Invalid Number


"""

def find_lucky(num):
    s = 0
    while num>0:
        digi = num%10
        s+=digi
        num//=10
    if s%2==0:
        return 1
    return 0

num = int(input("Enter the Number:"))
if num<=0:
    print("Invalid Number")
else:
    luck = find_lucky(num)
    if luck==1:
        print(f"{num} is lucky")
    else:
        print(f"{num} is not lucky")
