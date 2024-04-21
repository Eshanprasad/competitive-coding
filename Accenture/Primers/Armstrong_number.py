l = [int(x) for x in input("Enter the starting and ending numbers:\n").split()]
if l[0]<0 or l[1]<0:
    print("Starting and ending numbers must be greater than or equal to zero")
else:
    if l[0]>l[1]:
        print("Invalid input!! Ending number should be greater than starting number")
    else:
        num1, num2 = l[0], l[1]
        arm_numbers = []
        for i in range(num1, num2+1):
            sum_of_cubes = 0
            for j in str(i):
                sum_of_cubes+=(int(j)**3)
            if sum_of_cubes==i:
                arm_numbers.append(i)
        if arm_numbers:
            print(f"Armstrong numbers between {num1} and {num2} are:")
            for i in arm_numbers:
                print(i)
        else:
            print(f"Armstrong numbers between {num1} and {num2} are:")
            print("There is no Armstrong number between these numbers")
