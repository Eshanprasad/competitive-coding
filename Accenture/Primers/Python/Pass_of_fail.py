"""
Objective:

To work with Lists

Problem Description:

In a university exam of engineering students on various subjects, certain number of students passed in certain  subjects and failed in certain subjects. Taking one student into consideration,  write a simple program in Python  by using appropriate Python sequence to count the number of subjects he has passed and failed in.  Score 50 and below is considered fail. 
Guidelines:

If the no. of subjects is 0 or less display "Invalid no. of subjects" and terminate the program
if the mark is below 0 or above 100 , then display "Invalid mark" and terminate the program


Sample Input 1:

Enter the no. of subjects: 8

Enter the marks:

60

55

34

90

50

25

49

89

Sample Output 1:

No. of subjects passed: 4

No. of subjects failed: 4



Sample Input 2:

Enter the no. of subjects: 0

Sample Output 2:

Invalid no. of subjects



Sample Input 3:

Enter the no. of subjects: 10

Enter the marks:

10

0

5

109

Sample Output 3:

Invalid mark
"""



num_of_subs = int(input("Enter the no. of subjects: "))
if num_of_subs<=0:
    print("Invalid no. of subjects")
else:
    passed, failed = 0, 0
    print("Enter the marks:")
    for i in range(num_of_subs):
        a = int(input())
        if a>=0 and a<=100:
            if a>50:
                passed+=1
            else:
                failed+=1
        else:
            print("Invalid mark")
            break
    else:
        print("No. of subjects passed:", passed)
        print("No. of subjects failed:", failed)
