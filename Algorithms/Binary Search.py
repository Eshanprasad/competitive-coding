arr = [1,2,3,4,5,6,7,10,20]
x = 8
l = 0
r = len(arr)-1
while l <= r:
    mid = l + (r - l) // 2
    if arr[mid] == x:
        print(mid)
        break
    elif arr[mid] < x:
        l = mid + 1
    else:
        r = mid - 1
