"""
Create a sequence
1 4 10 19 31 46......N
Logic:
add multiples of 3
"""
N = int(input("enter length of sequence: "))
first = 1
count = 3
for i in range(N):
    print(first, end=" ")
    first+=count
    count+=3