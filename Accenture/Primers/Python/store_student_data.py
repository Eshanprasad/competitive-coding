"""
Objective:

To work with Files

Problem Description:

Wood Crust International School conducts a talent search test for middle school students.  The management wants to store students' names and their scores in the test in a file for their future reference.  You are asked to write a Python program to read the names and scores of the participants and store them in a file. Use simple write() to accomplish this task.

Note:
 The file name should be "output_data.txt"


Sample Input 1:
Enter the number of students: 3

For student 1
Enter name: Jane
Enter the score: 98

For student 2
Enter name: Lily
Enter the score: 99

For student 3
Enter name: Harry
Enter the score: 100


output_data.txt will contain:
Name:Jane Score: 98
Name: Lily Score: 99
Name: Harry Score: 100



Guidelines:

Step 1: Get the number of students from the user, convert that into an integer and store it in a variable

               no=int(input("Enter number of students: "))



Step 2: Open the file name in write mode to write the details.

              file=open('output_data.txt','w')



Step 3:  Using a for loop, obtain the user's name and grade for n students. Concatenate the name and score as specified in the problem description and write them into the 'output_data.txt' file one by one.Finally, close the opened file.

              for i in range(1,no+1):
                      print("Student"+str(i))
                      name=input("Enter name: ")
                      score=input("Enter the score: ")
                      data_format="Name: "+name+" "+"Score: "+score
                      file.write(data_format+"\n")
             file.close()           



Step 4: Then read the data from a file.  for this,  open the file in read mode, read all the data using the read() function, and display the data as provided in the problem description.  Finally, close the file.

               read_file=open("output_data.txt","r")
               data=read_data.read()
               print(data)
               read_file.close()
"""

num_of=int(input('Enter number of students: \n'))
file=open('output_data.txt','w')
for i in range(1,num_of+1):
    print(f'For student {i}')
    name=input('Enter name: \n')
    score=int(input('Enter the score: \n'))
    data_format=f'Name: {name} Score: {score}'
    file.write(f'{data_format}\n')
file.close()
read_file=open('output_data.txt','r')
data=read_file.read()
print('\noutput_data.txt will contain:')
print(data)
read_file.close()
