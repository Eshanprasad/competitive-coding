"""
Create a sequence
1 2 4 7 11......N

Logic:
add natural numbers
"""
N = int(input("enter length of sequence: "))
first = 1
count = 1
for i in range(N):
    print(first, end=" ")
    first+=count
    count+=1