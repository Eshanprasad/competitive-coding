"""
Objective:

To work with Files

Scenario:

"Roma" is a leading manufacturer of footwear in the City. The Company ships its products to various dealers across the world through Gaaty Shipments, a trusted brand in the logistics industry. It is customary for the footwear Company to prepare a list of their products to be shipped for that week, in a text file and send a copy of it across to Gaaty Shipments.

In connection with this, the footwear company's Manager intended to create a copy of this text file which contains all the product details to be shipped as
"Product - Product ID".
Help him by writing a program to copy the content from one file to another file.

For example, if the content of file_in.txt is
Aerosol - 38
Churn - 50
Plank - 55
Slipsheet - 75
Jerrican - 950
Girder - 100

the same should be copied to file_out.txt.

Input and Output Format :
Refer sample input and output for formatting specifications.

Sample Input :
No Input.
Read the content from file (file name) : file_in.txt.  The file is already been available in the platform

Sample Output :
In output file, the content will be copied.
Write the content to the output file (file name) : file_out.txt and display it.
Example:

Aerosol - 38
Churn - 50
Plank - 55
Slipsheet - 75
Jerrican - 950
Girder - 100
"""

with open('file_in.txt','r')as inputFile:
    with open('file_out.txt','w')as outputFile:
        for line in inputFile:
            outputFile.write(line)
with open('file_out.txt','r')as outputFile:
    print(outputFile.read())
