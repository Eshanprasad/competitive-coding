"""
Create a sequence
3 5 8 13 21 34 55......N

Logic:
add fibonacci sequence
"""
N = int(input("enter length of sequence: "))
first_val = 3
first = 1
second = 1
for i in range(N):
    print(first_val, end=" ")
    third = second + first
    first_val+=third
    first = second
    second = third

