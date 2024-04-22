"""
Objective:

To work with Lists

Problem Description:

A doctor survey results information is stored in 2 lists. First list represents all doctors ids (working and non -working both). Second list represents only working doctor's id. Please find the doctor ids who are not working.  Write a program in Python to perform the above task..
Input and Output Format:

First line of input corresponds to n1, the size of first list and next n1 lines correspond to the elements of the first list.

The next line corresponds to n2, the size of second list and next n2 lines correspond to the elements of the second list

Output is the id's of doctor who are not working

Guidelines:

1. Print "Invalid list size",  if the size of the list entered is a negative number  or zero and terminate the program

2. Print "Invalid Id", if the id entered is any negative number or zero, and terminate the program.



Sample Input 1:

7

7

2

3

4

5

6

1

3

3

4

5

Sample Output 1:

Not Working Doctors' IDs are:

7 2 6 1

 

Sample Input 2:

7

7

2

3

4

5

6

-1

Sample Output 2:

Invalid Id

 


Sample Input 3:

5

45

2

-5

Sample Output 3:

Invalid Id



Sample Input 4:

0

Sample Output 4:

Invalid list size

 

Sample Input 5:

3

67

44

33

-5

Sample Output 5:

Invalid list size



Sample Input 6:

3

15

36

78

2

0

Sample Output 6:

Invalid Id


"""


def main():
    n1 = int(input())
    if n1<=0:
        print("Invalid list size")
    else:
        all_doctors = []
        for i in range(n1):
            a = int(input())
            if a<=0:
                print("Invalid Id")
                quit()
            else:
                all_doctors.append(a)
        n2 = int(input())
        if n2 <= 0:
            print("Invalid list size")
        else:
            working_doc = []
            for i in range(n2):
                a = int(input())
                if a <= 0:
                    print("Invalid Id")
                    quit()
                else:
                    working_doc.append(a)
            for i in working_doc:
                if i in all_doctors:
                    all_doctors.remove(i)
            print("Not Working Doctors' IDs are:")
            for i in all_doctors:
                print(i, end=" ")
    return

if __name__ == '__main__':
    main()
