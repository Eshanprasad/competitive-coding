"""
Objective:

To work with Functions

Problem Description:

Imagine D Iman, a famous music director to be composing a pop album. To create a unique composition, he decides to play only those keys of his instrument (consider every key has a number associated with it) which are divisible by one and itself (i.e. prime numbers). You may help him by writing a program in Python to print all the numbers that represent the keys he will need for his new composition - given the interval [start, end] (start and end inclusive) within which he chooses the keys.   Write a user-defined function to find out the key with prime numbers.
Guidelines:

If the start or end number is negative, then display the message "Invalid range".
If there are no prime numbers between the starting and ending range, then display the message "There are no prime numbers in this range".
 If the start and end numbers are the same, then display the message "There are no prime numbers in this range".
If the start number is greater than the end number, then display the message "Invalid range".
The function definition should be: find_prime(start, end) -  This function should take the start and end numbers as parameters and return the prime numbers as a list.
Refer to the sample input and output statements for more clarifications.

Sample Input 1:

2

11

Sample Output 1:

2 3 5 7 11

Sample Input 2:

3

-10

 Sample Output 2:

Invalid range



Sample Input 3:

0

1

Sample Output 3:

There are no prime numbers in this range
Sample Input 4:

1

1

Sample Output 4:

There are no prime numbers in this range

Sample Input 5:

1

11

Sample Output 5:

2 3 5 7 11
"""


def find_prime(n1, n2):
    if n1 < 0 or n2 < 0:
        return ['Invalid range']
    if n1 > n2:
        return ['Invalid range']
    prime = []
    for num in range(n1, n2 + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime.append(num)
    if not prime:
        return ['There are no prime numbers in this range']
    return prime

start = int(input('\n'))
end = int(input('\n'))
x = find_prime(start, end)
result = ''
for i in range(len(x)):
    result += str(x[i]) + ' '
print(result.strip())
