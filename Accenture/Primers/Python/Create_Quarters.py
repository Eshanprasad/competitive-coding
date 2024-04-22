"""
Objective:

To work with Tuples

Problem Description:

Ms. Ann wants her students to understand about tuples in Python.  She wanted them to create a tuple  with the name 'months'  which should contain the name of all 12 months.    She also wanted them to slice this tuple into four quarters :  January - March, April - June, July - September and October - December.  Store these quarters into 4 different tuples and display all the tuples as specified in the sample output.    

Sample Output:
Months in expanded form:                                                       
January                                                                        
February                                                                       
March                                                                          
April                                                                          
May                                                                            
June                                                                           
July                                                                           
August                                                                         
September         
October
November
December

The four quarters are:

First Quarter :
January
February
March

Second Quarter :
April
May
June

Third Quarter :
July
August
September

Fourth Quarter :
October
November
December

"""

months = ('January','February','March','April','May', 'June','July','August','September','October','November','December')
print("Months in expanded form:")
for i in months:
    print(i)
print()
print("The four quarters are:")
print()
print("First Quarter :")
for i in months[:3]:
    print(i)
print()
print("Second Quarter :")
for i in months[3:6]:
    print(i)
print()
print("Third Quarter :")
for i in months[6:9]:
    print(i)
print()
print("Fourth Quarter :")
for i in months[9:]:
    print(i)
