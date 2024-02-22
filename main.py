arr = [5,3,4,5,2,6, 1, 1]
first = 10000   #assuming 10000 is max number
second = 10000  #assuming 10000 is max number
for i in range(0, len(arr)):
    if arr[i] < first:
        second = first
        first = arr[i]
    elif (arr[i] < second):
        second = arr[i]