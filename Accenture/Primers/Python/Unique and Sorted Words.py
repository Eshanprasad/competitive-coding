"""
Objective:

To work with Set

Problem Description:

Write a Python program that accepts a sequence of white-space-separated words/numbers as input and displays the words/numbers after removing all the duplicates and sorting them alpha-numerically.
For example, if the following input is supplied to the program:

"hello world and practice makes perfect and hello world again"    

The output should be:  

again and hello makes perfect practice world


Guidelines:   

1. Use Python 'set' data structure to remove the duplicate data automatically and then sort the data.
2. No need to consider the cases of strings.  That is "WorLd" and "world" should be considered as same.


Sample Input 1:
Enter the string:
hello world and practice makes the man perfect and hello world again

Sample Output 1:
again and hello makes man perfect practice the world


Sample Input 2:
Enter the string: 
123 456 123 321

Sample Output 2:
123 321 456


"""
"""
what I learned from solving this code is:
if a string s= "123"
then if we execute s.lower(), it works fine and throws No Error. Output of it is just "123"
"""


#solution
s = set([x for x in input("Enter the string:\n").lower().split()])
l = list(s)
print(' '.join(sorted(l)))




