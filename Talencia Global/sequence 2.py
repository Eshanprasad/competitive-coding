"""
Create a sequence
6 8 11 16 23 34 47 64......N
Logic:
add prime numbers
"""

N = int(input("enter length of sequence"))
first = 6
prime_list = []
i = 2
while len(prime_list)<N:        #this loop stores all prime numbers required to get "N" number of sequence
    if all(i%j!=0 for j in range(2, i)):
        prime_list.append(i)
        i+=1
    else:
        i+=1
for i in range(N):
    print(first, end=" ")
    first+=prime_list[i]