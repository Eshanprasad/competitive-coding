"""
Objective:

To work with dictionaries



Problem Description:

Ms. Ann wants her students to have a clear understanding of dictionary data structure in python.  She tells them to create a dictionary by the name 'word_dictionary' - consisting of words and the associated meaning(s).  The word becomes the key and the list of associated meanings becomes values pertaining to that key.  A dictionary can contain  N number of key-value pairs.   Refer to the sample input and output for more clarifications and write the program accordingly.



Note : 

If the no. of meanings entered is zero or negative, then display the message "Invalid Input" and display the contents of the dictionary ( key-value pairs) currently present (if any). 
When you want to add more elements to the dictionary, you have to enter '1' else you need to enter '0'.  If you enter '1', the program should continue asking about the word and its meanings or if you enter '0' then display the list of dictionaries.  If the choice is not '0' or '1',  then display the message "Invalid Input" followed by the contents of the list of dictionaries.  Refer to the sample input and output for more clarifications.  


Sample Input 1:

Enter the word: Python

Enter the no of meanings: 2

Enter the meanings :

A large heavy-bodied non-venomous snake occurring throughout the Old World tropics, killing prey by constriction and asphyxiation

A high-level general-purpose programming language

Do you want to add one more elements to the dictionary? If yes, press 1, else press 0: 1

Enter the word: ape

Enter the no of meanings: 3

Enter the meanings :

A large primate that lacks a tail, including gorilla, chimpanzees, orangutan, and gibbons

An unintelligent or clumsy person

Imitate (someone or something), especially in an absurd or unthinking way
Do you want to add one more elements to the dictionary? If yes, press 1, else press 0: 0



Sample Output 1:

Here's the dictionary you've created:

Python : ['A large heavy-bodied non-venomous snake occurring throughout the Old World tropics, killing prey by constriction and asphyxiation', 'A high-level general-purpose programming language']  

ape : ['A large primate that lacks a tail, including the gorilla, chimpanzees, orangutan, and gibbons', 'An unintelligent or clumsy person', 'Imitate (someone or something), especially in an absurd or unthinking way']



Sample Input 2:

Enter the word: Hello world
Enter the no of meanings:0

Sample Output 2:

Invalid Input



Sample Input 3:

Enter the word: Hello world
Enter the no of meanings:1
Enter the meanings:
Saying hello to the world

Do you want to add one more elements to the dictionary? If yes, press 1, else press 0:
2


Sample Output 3:

Invalid Input
Here's the dictionary you've created:
Hello world: ['Saying hello to the world']

"""

def main():
    ### Write your code here
    word_dictionary={}
    while True:
        word=input('Enter the word:\n')
        no_of_meanings=int(input('Enter the no of meanings:\n'))
        if no_of_meanings<=0:
            print('Invalid Input')
            for key,value in word_dictionary.items():
                print(f'{key}:{value}')
            break
        else:
            meanings=[]
            print('Enter the meanings:')
            for i in range(no_of_meanings):
                data=input()
                meanings.append(data)
            word_dictionary[word]=meanings
            choice=int(input('Do you want to add one more elements to the dictionary? If yes, press 1, else press 0:\n'))
            if choice==1:
                continue
            elif choice==0:
                print("Here's the dictionary you've created:")
                for key,value in word_dictionary.items():
                    print(f'{key}:{value}')
                break
            else:
                print('Invalid Input')
                print("Here's the dictionary you've created:")
                for key,value in word_dictionary.items():
                    print(f'{key}:{value}')
                break
    return



if __name__=='__main__':
    main()
