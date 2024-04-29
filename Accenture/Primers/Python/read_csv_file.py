"""
Objective:

To work with Files



Problem Description:

Sachin R Tendulkar made his ODI debut in 1989. OneDayInternational.csv is a CSV file containing about 200 records on Sachin's ODIs from 1990 to 1998.  Read this CSV file using DictReader() and display the contents in the first 10 rows.
Here is the sample of first 2 records from OneDayInternational.csv

Country    Player                             Runs    ScoreRate          MatchDate    Ground                 Versus    URL
Ind             Sachin R Tendulkar    0           0                           1/3/1990        Carisbrook          NZ            673
Ind             Sachin R Tendulkar    36        92.30769231    6/3/1990        Basin Reserve    NZ           676
"""

import csv
with open('OneDayInternational.csv','r')as csvFile:
    csv_read = csv.DictReader(csvFile)
    count=0
    for i in csv_read:
        print(i)
        count+=1
        if count==10:
            break
