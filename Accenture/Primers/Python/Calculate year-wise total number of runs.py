"""
Objective:

To work with Files



Problem Description:

OneDayInternational.csv is a CSV file containing about 200 records on Sachin's ODIs from 1990 to 1998. Read this CSV file using DictReader() and calculate the year-wise total number of runs Sachin. Display the same in the following format: 
1990 239
1991 417
.......
"""
import csv

year_runs={}
with open('OneDayInternational.csv','r')as csv_file:
    csv_reader=csv.DictReader(csv_file)
    for row in csv_reader:
        year=row['MatchDate'].split('/')[2]
        runs=int(row['Runs'])
        year_runs[year]=year_runs.get(year,0)+runs
for year,runs in sorted(year_runs.items()):
    print(year,runs)
