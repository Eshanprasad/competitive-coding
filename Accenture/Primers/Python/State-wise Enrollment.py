"""
Objective:

To work with dictionaries



Problem Description:

To conduct a musical competition for people in the age group of 11-80 all over the country, a famous channel needs to collect the name, age, and state of the people who enrolled for the competition.  They also want to know the number of participants enrolled from each state of the country. This analysis will help them to conduct audition centers at the right places. 
Write a Python program to store the name, age, and state of the enrolled candidates of the competition in a list of dictionaries - with keys - 'Name', 'Age', and 'State'  and find out the number of participants enrolled from each state. 



Note:

If the no. of participant details to be created is entered as zero or negative number, then display the message "Invalid Input" and display the key-value pairs currently present in the dictionary (if any).
If the age of the participant entered is <=10 and >80, display "Invalid Input" and then display the key-value pairs "currently" present in the dictionary (if any).            
 

Sample Input:

Enter the no. of participants details to be created :3
Name: Ronn
State: Berkshire
Age: 23
Name: Harry
State: Berkshire
Age: 27
Name: Jane
State: Moray
Age: 25


Sample Output:

Here's the list of participants' details :
{'Name': 'Ronn', 'State': 'Berkshire', 'Age': 23}
{'Name': 'Harry', 'State': 'Berkshire', 'Age': 27}
{'Name': 'Jane', 'State': 'Moray', 'Age': 25}
State:  Berkshire   Count:  2
State:  Moray  Count:  1


Guidelines:

Step 1: In the main method get the number of participants from the user, convert that into an integer and store it in a variable as:

              n=int(input("Enter the no of participants details to be created : ")) 

Step 2: Create an empty  student list for storing details:

              student_list=[] 

Step 3:  If the number of participants is greater than 0, then get the name, state, and age from the user using a loop.

               if n>0:
                     for i in range No:
                           student={}
                           name=input("Name: ")
                           state=input("State: ")
                           age=int(input("Age: "))

Step 4: If the age is less than or equal to 10 and greater than 80, then display the message "Invalid input" and continue the loop.

                           if age<=10 and age>80:
                                print("Invalid input")
                                continue

Step 5: Otherwise, create a dictionary with keys as 'Name','State', and 'Age' and values as the corresponding input values. Then append that dictionary to a student list.
                         student["Name"]=name
                         student["State"]=state
                         student["Age"]=age
                         student_list.append(student)

Step 6: Then iterate through the student list, displaying each participant's information as per the sample input and output statements.
                 print("Here's the list of participants details:")
                 for i in student_list:
                        print(i)

  

Step 7: Create a new empty dictionary and iterate through the student list, checking to see if the state is in the new dictionary. If the state is not in the new dictionary, then add the state as a key and 1 (count) as a value. Otherwise, increment the corresponding state's count.

                res={}
                for i in student_list:
                          if i["State"] not in res.keys():
                                res[i["State"]]=1
                          else:
                                 res[i["State"]]=res[i["State"]]+1                              


Step 8: Then iterate the dictionary to display the state and corresponding count as per the sample input and output statements.

                  for key,value in res.items():
                           print("State: ",key,"Count: ",value)

     

Step 9: If the number of participants is less than or equal to 0, then display the message as "Invalid input".                    else:
                 print("Invalid input")
"""

def main():
    ### Write your code here
    n=int(input('Enter the no of participants details to be created :\n'))
    student_list=[]    
    if n>0:
        for i in range(n):
            student={}
            name=input('Name:\n')
            state=input('State:\n')
            age=int(input('Age:\n'))
            if age<=10 or age>80:
                print('Invalid input')
                continue
            student['Name']=name
            student['State']=state
            student['Age']=age
            student_list.append(student)
        print("Here's the list of participants details:")
        for i in student_list:
            print(i)
        res={}
        for i in student_list:
            if i['State'] not in res.keys():
                res[i['State']]=1
            else:
                res[i['State']]=res[i['State']]+1
        for key,value in res.items():
            print('State:',key,'Count:',value)
    else:
        print('Invalid input')
    return



if __name__=='__main__':
    main()
