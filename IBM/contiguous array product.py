"""
contiguous subarrays are a group of an uninterrupted range of elements from an
array as they occur. No elements in the range can be skipped or reordered.
Given an array of integers, numbers, and an integer k, determine the total number of
subarrays of numbers that have a product that is less than or equal to k.

Example:
numbers = [2,3,4]

the sub arrays are [2], [3], [4], [2,3], [3,4], [2,3,4]
the product of those respective subarrays are 2, 3, 4, 6, 12, 24.

4 subarrays satisfy the condition [2], [3], [4], [2,3].

"""
l = [int(x) for x in input().split()]
k = int(input())
out = []
count = 0
for i in range(len(l)):
    for j in range(i+1, len(l)+1):
        out.append(l[i:j])
for i in out:
    prod = 1
    for j in i:
        prod*=j
    if prod<=k:
        count+=1
print(count )