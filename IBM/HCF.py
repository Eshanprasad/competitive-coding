"""
1. Write a program to find HCF of two numbers by without using recursion.
Input format:
The first line contains any 2 positive numbers separated by space.
Output format:
Print the HCF of given two numbers.
Sample Input:
70 15
Sample Output:
5
"""
l = [int(x) for x in input().split()]
H = 1
for i in range(min(l[0], l[1])+1, 0, -1):
    if l[0]%i==0 and l[1]%i==0:
        H = i
        break
print(H)
