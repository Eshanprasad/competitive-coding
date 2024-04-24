"""
Objective:

To work with Functions

Problem Description:

Write a function 'concat_string(string1,string2)' which will accept two strings from the user.  This function should return the concatenated string of string1 and string2 by eliminating the first two characters from both the strings and the length of the concatenated string.
Guidelines:

1.  The string names should be 'string1' for the first input and 'string2' for the second input (inputs should be user input).

2.  The concat_string(string1,string2) should return the concatenated string of 'string1' and 'string2' by eliminating the first two characters from both and the length of the concatenated string.  Refer to the sample input and output statements for more clarifications.

 3.  Strictly follow the naming conventions for variables and functions as specified in the problem description.



Sample Input 1:

Enter String1: Hai

Enter String2: how are you

Sample Output 1:

The concatenated string: iw are you

The length of the new string is :10



Sample Input 2:

Enter String1: Hello

Enter String2: desire

Sample Output 2:

The concatenated string: llosire

The length of the new string is : 7

"""



def concat_string(string1,string2):
    string3 = string1[2:] + string2[2:]
    l = len(string3)
    return (string3, l)


def main():
    string1 = input("Enter String1: ")
    string2 = input("Enter String2: ")
    result = concat_string(string1, string2)
    print("The concatenated string:", result[0])
    print("The length of the new string is :", result[1])
    return

if __name__=="__main__":
    main()
