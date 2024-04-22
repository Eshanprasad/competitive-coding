"""
Objective:

To work with Lists

Problem Description:

AEIMA's collection of professional development courses is the ideal solution for today's busy professionals who do not have time to sit in a conventional classroom, yet want a high-quality education in the professional development front.  AEIMA's online courses are offered exclusively online and are to be completed through self-paced study.  AEIMA does not have a formal enrollment process. All the courses are available to all the students and a student may choose to purchase one or more courses or all of them.  Write a program in Python to create a report for a student, on his course completion. The report must contain the no. of courses, course names, and marks pertaining to each course. However, the report displayed to the student must only contain the details of the course(s) in which he has scored 80% and above.
Guidelines:

1. If the user enters no. of courses to be less than 1, then display "Invalid no. of courses" and terminate the program

2. If the mark specified is less than 0 or greater than 100, display "Invalid mark" and terminate the program.



Sample Input 1:

Enter the number of courses: 4
Enter the name of the subject and marks respectively:
Python
98
Enter the name of the subject and marks respectively:
C Programming
79
Enter the name of the subject and marks respectively:
Java
85
Enter the name of the subject and marks respectively:
C
56

Sample Output 1:
The courses you have cleared are:
Python 98
Java 85

 
Sample Input 2:

Enter the number of courses: 2

Enter the name of the subject and marks respectively:

Java

-1

Sample Output 2:
Invalid mark

 

Sample Input 3:

Enter the number of courses: 0

Sample Output 3:

Invalid no. of courses


Sample Input 4:

Enter the number of courses: 3

Enter the name of the subject and marks respectively:

Mathematics

22

Enter the name of the subject and marks respectively:

Science

101

Sample Output 4:

Invalid mark
"""


num=int(input('Enter the number of courses: '))
if num<1:
    print('Invalid no. of courses')
    quit()
else:
    courses,marks=[],[]
    for i in range(num):
        print('Enter the name of the subject and marks respectively:')
        sub=input()
        m=int(input())
        if m<0 or m>100:
            print('Invalid mark')
            quit()
        else:
            courses.append(sub)
            marks.append(m)
    print('The courses you have cleared are:')
    for i in range(num):
        if marks[i]>=80:
            print(courses[i],marks[i])
