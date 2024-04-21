"""
Objective:

To work with Control structures

Problem Description:

Renn plans a trip to Goa, this weekend. He decides to go by bus and book his ticket through a website. Code logic in Python so that he gets to know if he has booked a window seat or not.  

Assume the bus to have 11 rows.  Seat number begins with 1 which will be a window seat.  If the no. of seats per row is a factor of the seat number you have entered, then it is a window seat, else it is not a window seat.   Refer to the sample input and output statements for more clarifications.

Guidelines:
1. For any invalid seat number specified is a negative number, zero or the seat number is greater than total no. of seats, then display - "Invalid Seat Number" and stop the program.

2. If the no. of seats per row specified is less than or equal to zero, then display - "Invalid Input" and stop the program.

 
Sample Input 1:
Enter the number of seats per row
4
Enter the seat number
36

Sample Output 1:
Window Seat


Sample Input 2:
Enter the number of seats per row
3
Enter the seat number
20

Sample Output 2:
Not a Window Seat


Sample Input 3:
Enter the number of seats per row
4
Enter the seat number
48

Sample Output 3:
Invalid Seat Number

"""



number_of_seats = int(input("Enter the number of seats per row\n"))
if number_of_seats<=0:
    print("Invalid Input")
else:
    seat_num = int(input("Enter the seat number\n"))
    if seat_num<=0 or seat_num>(11*number_of_seats):
        print("Invalid Seat Number")
    else:
        if seat_num%number_of_seats==0:
            print("Window Seat")
        else:
            print("Not a Window Seat")
