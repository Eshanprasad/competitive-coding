"""
Objective:

To work with Files



Problem Description:

OneDayInternational.csv is a CSV file containing nearly 200 records on Sachin's ODIs from 1990 to 1998.  Read this CSV file using DictReader() and filter the countries he has played against, order them alphabetically and display them!


Here is the sample of the first 2 records from OneDayInternational.csv

Country    Player                             Runs      ScoreRate         MatchDate     Ground                   Versus    URL
Ind             Sachin R Tendulkar    0             0                          1/3/1990         Carisbrook            NZ            673
Ind             Sachin R Tendulkar    36          92.30769231   6/3/1990         Basin Reserve     NZ            676
"""

import csv

with open('OneDayInternational.csv','r')as csv_file:
    csv_reader=csv.DictReader(csv_file)
    countries=set()
    for row in csv_reader:
        countries.add(row['Versus'])
    countries=sorted(countries)
    print(countries)
