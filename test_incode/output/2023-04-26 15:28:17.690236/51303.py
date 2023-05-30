#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates user input. """    
    
    # Read user input
    user_input = input('Enter your choice: ')
    
    # Print user input
    print('Your choice is: ', user_input)
    
    # Print the list of choices
    print('The list of choices are: ')
    for choice in choices:
        print(choice)
    
    # Print the list of choices with their counts
    print('The list of choices with their counts are: ')
    for choice in choices:
        print(choice, choices[choice])
    
    # Print the list of choices with their counts and their 