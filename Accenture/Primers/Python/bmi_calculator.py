"""
Objective:

To work with Control structures



Problem Description:

Program in Python to compute the BMI of a person and display the  risk associated with it by entering the height in 'm' and weight in' kg'. Refer the following table and code accordingly.

Guidelines:

To calculate the BMI apply the formula:  BMI = weight(kg)/( height(m)*height(m) ).    
Result must be adjusted to one decimal place. 
When the height or weight is entered as a negative number or  zero, then display the message "Provide a valid input" and stop the program.


BMI

Risk

27.5 and above

High Risk

23 - 27.4

Moderate Risk

18.5 - 22.9

Low Risk

Below 18.5

Risk of nutritional deficiency diseases




Sample Input 1:
Enter the weight of the person(kg):85

Enter the height of the person(m):1.75

Sample Output 1:

Your BMI is 27.8 (High Risk).

Sample Input 2:

Enter the weight of the person(kg):0

Enter the height of the person(m):1.58

Sample Output 2:

Provide a valid input



Sample Input 3:

Enter the weight of the person(kg):80

Enter the height of the person(m):-1

Sample Output 3:

Provide a valid input

"""

weight = int(input("Enter the weight of the person(kg):"))
height = float(input("Enter the height of the person(m):"))
if weight<=0 or height<=0:
    print("Provide a valid input")
else:
    bmi = weight/(height*height)
    BMI = round(bmi, 1)
    if BMI >= 27.5:
        print("Your BMI is " + str(BMI) + " (High Risk).")
    elif BMI >= 23 and BMI <= 27.4:
        print("Your BMI is " + str(BMI) + " (Moderate Risk).")
    elif BMI >= 18.5 and BMI <= 22.9:
        print("Your BMI is " + str(BMI) + " (Low Risk).")
    elif BMI < 18.5:
        print("Your BMI is " + str(BMI) + " (Risk of nutritional deficiency diseases).")
