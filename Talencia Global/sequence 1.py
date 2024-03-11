"""
create a sequence
1 3 7 13 ..... N

logic: +2 +4 +6 ....
"""
n = int(input())
first = 1
count = 2
for i in range(n):
    print(first, end=" ")
    first += count
    count += 2