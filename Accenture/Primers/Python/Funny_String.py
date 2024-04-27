"""
Objective:

To work with functions

Problem Description:

Roshan plays an interesting game using strings.  He has a string, STR1 of length 'L' that is indexed from 0 to L-1. He also has another string, STR2 which is the reverse of String STR1.  He needs to find out if the string STR1 is funny. This means if the condition: STR1[i]-STR1[i-1]==STR2[i]-STR2[i-1] is true for every character i from 1 to L-1, then the string is said to be funny. 

Constraints:
1. The length should be a minimum of 2 and a maximum of 50. 
2. The function definition should be: funny_string(string) which should return the string 'Funny' or 'Not Funny' according to the string.
Sample Input 1:
Enter the string:acxz

Sample Output 1:
Funny



Sample Input 2:
Enter the string:bcxz

Sample Output 2:
Not funny


Sample Input 3:
Enter the string:acegvxz

Sample Output 3:
Not funny



Sample Input 4:
Enter the string:zwtqjgda

Sample Output 4:
Funny



Sample Input 5:
Enter the string:s

Sample Output 5:
Invalid string
"""

STR1 = input("Enter the string:").lower()
if len(STR1)<=1 or len(STR1)>50:
    print("Invalid string")
    quit()
STR2 = STR1[::-1]
s = "abcdefghijklmnopqrstuvwxyz"
d = {}
count = 1
for i in s:
    d[i] = count
    count+=1
for i in range(1, len(STR1)):
    if abs(d[STR1[i]]-d[STR1[i-1]]) != abs(d[STR2[i]]-d[STR2[i-1]]):
        print("Not funny")
        break
else:
    print("Funny")
