"""
Objective:

To work with conditional and looping statements



Problem Description:

The state committee announced that all people should get vaccinated against corona-19. So the state's area counselor wanted to know the number of non-vaccinated people in his area, as well as the percentage of people who have received two doses of vaccine.

Write a Python program that helps the counselor get the details of vaccinated and non-vaccinated people. Refer to the sample input and output statements for more clarification.



Note:

If the total number of people in the area is less than or equal to 0, then it displays the message "Invalid input" and terminates the program.
If the single-dose count is less than 0 or greater than the total number of people count, then display the message "Invalid input" and terminate the program.
If the double dose count is less than 0 or greater than the total number of people count, then display the message "Invalid Input" and terminate the program.
If single and double dose total counts are greater than the total area count, then it should display the message "Invalid Input" and terminate the program.

If the councilor needs to collect details of the next area, then he needs to press  "1", else press " 0" to terminate the program.

If he enters anything other than '0' or '1', it should display the message as "Invalid Input" and terminate the program.
Use the 'break' statement to terminate the program.
Total vaccinated percentage of people should be calcualted by (double dose count/total no of people)*100


Sample Input and output statement 1:

Enter the total no of people in the area: 60

Single-dose count: 20

Double-dose count: 40



Not vaccinated people count:  0

Total vaccinated percentage of people: 66.67



Do you want to continue (1) for yes (0) for no: 1

Enter the total no of people in the area: 50

Single-dose count:27

Double-dose count:20



Not vaccinated people count:  3

Total vaccinated percentage of people:40.00

Do you want to continue (1) for yes (0) for no: 0

 

Sample Input and output statement 2:

Enter the total no of people in the area: -3

Invalid Input

 

Sample Input and output statement 3:

Enter the total no of people in the area: 30

Single-dose count: 5

Double-dose count: 35

Invalid Input


Sample Input and output statement 4:

Enter the total no of people in the area: 30

Single-dose count: 5

Double-dose count: 28

Invalid Input


"""

while True:
    num_of_people = int(input("Enter the total no of people in the area: "))
    if num_of_people<=0:
        print("Invalid input")
    else:
        single_dose = int(input("Single-dose count: "))
        if single_dose<0 or single_dose>num_of_people:
            print("Invalid input")
        else:
            double_cose = int(input("Double-dose count: "))
            if double_cose<0 or double_cose>num_of_people:
                print("Invalid Input")
            else:
                if single_dose+double_cose>num_of_people:
                    print("Invalid Input")
                else:
                    print()
                    print("Not vaccinated people count: ", num_of_people-single_dose-double_cose)
                    print("Total vaccinated percentage of people: {:.2f}".format((double_cose/num_of_people)*100))
                    val = input("Do you want to continue (1) for yes (0) for no: ")
                    if val=="1":
                        continue
                    elif val == "0":
                        break
                    else:
                        print("Invalid Input")
                        break
