"""
Objective:

To work with JSON files



Problem Description:

"LC BANKING SOLUTIONS" is one of the new banks started in the city, they are in need of an automated system that should filter the bank customers based on loan type.

You being their software consultant have been approached to develop a Python application that can be used by the admin for the above-mentioned requirement.

This functionality deals with getting the loan_type from the user and filtering the customers based on loan type by reading the JSON file which is available in our platform in the following format.

 File name: loan.json

{

  "customers": [

    {

      "Account_Number": "1111101015923",

      "customer_name": "Anish",

      "loans": [

        {

          "loan_amount": 300000,

          "loan_id": "1001",

          "loan_type": "housing"

        },

        {

          "loan_amount": 100000,

          "loan_id": "1110",

          "loan_type": "Personal"

        }

      ]

    },

    {

    "Account_Number": "1111101010001",

    "customer_name": "Daniel",

      "loans": [

        {

          "loan_amount": 200000,

          "loan_id": "1010",

          "loan_type": "Personal"

        },

        {

          "loan_amount": 300000,

          "loan_id": "1000",

          "loan_type": "Educational"

        }

      ]

    },

    {

      "Account_Number": "1111101011113",

      "customer_name": "Joe",

      "loans": [

        {

          "loan_amount": 500000,

          "loan_id": "1331",

          "loan_type": "Housing"

        }

      ]

    }

  ]

â€¦

â€¦

â€¦

} 

Perform the below operations:

1. Get the loan_type as user input and store it into a variable.  The variable name should be 'loan_type'.

2. filter_customers(loan_type): This method should take loan_type as its argument and should filter the customers based on loan type by reading the 'loan.json' file given and it should display the customer details corresponding to loan_type passed as an argument, if there are no customers based on particular loan type the function should display "No customers available".

Strictly follow the naming conventions for variables and functions as specified in the problem description.



Sample Input and Output 1:

Enter the loan type

housing

Loan Details

Account_Number     Customer_Name   Loan_Amount

1111101015923       Anish                   300000

1111101011113       Joe                      500000



Sample Input and Output 2:

Enter the loan type

Jewelry

No customers available
"""

import json
def filter_customers(loan_type):
    with open('loan.json') as json_file:
        data = json.load(json_file)
        customers = data['customers']
        count = 0
        for customer in customers:
            loans = customer['loans']
            for loan in loans:
                if loan['loan_type'].lower() == loan_type:
                    count += 1
        if count == 0:
            print('No customers available')
        else:
            print('Loan Details')
            print('Account_Number\tCustomer_Name\tLoan_Amount')
            for customer in customers:
                loans = customer['loans']
                for loan in loans:
                    if loan['loan_type'].lower() == loan_type:
                        print(customer['Account_Number'], '\t', customer['customer_name'], '\t', loan['loan_amount'])

loan_type = input('Enter the loan type\n')
filter_customers(loan_type)
