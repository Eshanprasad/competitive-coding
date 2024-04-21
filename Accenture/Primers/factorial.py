number = int(input("Enter a number\n"))
if number<0:
    print("Factorial does not exist for negative numbers")
else:
    if number==0:
        print("Factorial is 1")
    else:
        prod = 1
        for i in range(number, 0, -1):
            prod*=i
        print("Factorial is", prod)
