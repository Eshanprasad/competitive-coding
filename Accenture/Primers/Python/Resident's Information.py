"""
Objective:

To work with Lists and tuples

Problem Description:

Mr. Joe wants to collect the details of Central Government employees in his locality  - that includes their name, age, designation, and band. He wants to view this information as a whole and also with respect to bands.

Write a Python program to accomplish the same. Create a list of tuples with the name  'List_of_Residents'  to store the information obtained from the residents. Use insert() to insert tuples into this list. Observe the sample input and output and code accordingly.

Guidelines:
1. If the age provided is not between 21 and 58, display 'Invalid"  and stop the program.
2. If the band entered by the user and the interested band the user entered is not A, B, C, or D, display 'Invalid" and stop the program.
3. If the valid band asked for is absent in the list of residents - details created, 'No resident under this band'
4. If the no. of residents provided is not equal to or above zero, display 'Invalid" and stop the program.

Sample Input 1:
No of Residents: 5
    
Resident 1:
Name : Mr. Ram
Age : 30
Designation : Commissioned Officer - IAF
Band : A

Resident 2:
Name : Mr. Raj
Age : 35
Designation :  Inspector of Income Tax
Band : B

Resident 3:
Name : Mr. Alex
Age : 40
Designation : Central Excise Inspector
Band : B

Resident 4:
Name : Mr. Joe
Age : 45
Designation : Stenographer
Band : C

Resident 5:
Name : Mr. Ali
Age : 42
Designation : Peon
Band : D

Sample Output 1:
('NAME', 'AGE', 'DESIGNATION', 'BAND')
('Mr. Ram', 30, 'Commissioned Officer - IAF', 'A')
('Mr. Raj', 35, 'Inspector of Income Tax', 'B')
('Mr. Alex', 40, 'Central Excise Inspector', 'B')
('Mr. Joe', 45, 'Stenographer', 'C')
('Mr. Ali', 42, 'Peon', 'D')

Enter your band of interest : B
('NAME', 'AGE', 'DESIGNATION', 'BAND')
('Mr. Raj', 35, 'Inspector of Income Tax', 'B')
('Mr. Alex', 40, 'Central Excise Inspector', 'B')

Sample Input 2:
No of Residents :2

Resident 1:
Name :David
Age :23
Designation :PRO
Band :A

Resident 2:
Name :Raj
Age :34
Designation :RMO
Band :C

Sample Output 2:
('NAME','AGE','DESIGNATION','BAND')
('David', 23, 'PRO', 'A')
('Raj', 34, 'RMO', 'C')

Enter your band of interest :B
('NAME', 'AGE', 'DESIGNATION', 'BAND')
No resident under this band

"""

no_of_residents=int(input('\nNo of Residents :\n'))
residents_list=[]
if no_of_residents<=0:
    print('Invalid')
    quit()
for i in range(no_of_residents):
    print(f'Resident {str(i+1)}:')
    name=input('Name :\n')
    age=int(input('Age :\n'))
    if age<21 or age>58:
        print('Invalid')
        quit()
    designation=input('Designation :\n')
    band=input('Band :\n')
    if band not in ('A','B','C','D'):
        print('Invalid')
        quit()
    resident=(name,age,designation,band)
    residents_list.insert(i,resident)
print("('NAME','AGE','DESIGNATION','BAND')")
for i in residents_list:
    print(i)
band_interest=input('Enter your band of interest:\n')
if band_interest not in ('A','B','C','D'):
    print('Invalid')
    quit()
else:
    band_count=0
    print("('NAME','AGE','DESIGNATION','BAND')")
    for i in residents_list:
        if band_interest in i:
            print(i)
            band_count+=1
    if band_count==0:
        print('No resident under this band')
