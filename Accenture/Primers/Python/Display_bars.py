'''
Objectives:

To work with functions



Problem Description:

Write a Python program to create different types of bars.   for this create a module in Python named 'bars.py' which should contain a function that takes 3 parameters for drawing 3 different types of bars. You may use the symbols '*' for creating the star bar,  '-'  for drawing the hyphen bar, and '#' for drawing a hash bar.  Refer to the sample input and output statements for more details.

Inside the module - bars.py, the method signature should be: draw_bar(n1,n2,n3) where:

n1 - number of times  the symbol '*' should display

n2 - number of times  the symbol '-' should display

n3 - number of times  the symbol '#' should display

Note:  'visualize.py' must contain relevant print statements and the function calls.


Sample Input 1:
Enter the no. of times '*' should display:12
Enter the no. of times '-' should display:2
Enter the no. of times '#' should display:4

Sample Output 1:
************

--

####



Sample Input 2 :

Enter the no. of times '*' should display:10
Enter the no. of times '-' should display:5
Enter the no. of times '#' should display:0

Sample Output 2:
**********

-----
'''



#visualize.py
def main():
    n1 = int(input("Enter the no. of times '*' should display:"))
    n2 = int(input("Enter the no. of times '-' should display:"))
    n3 = int(input("Enter the no. of times '#' should display:"))
    bars.draw_bar(n1, n2, n3)


#bars.py
def draw_bar(n1,n2,n3):
    print('*'*n1)
    print('-' * n2)
    print('#'*n3)
