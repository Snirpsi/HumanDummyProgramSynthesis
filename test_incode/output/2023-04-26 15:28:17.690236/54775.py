#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes user input. """    
    
    # Get the input from the user
    user_input = input('Enter a number: ')
    
    # Convert the input to an integer
    number = int(user_input)
    
    # Remove the user input
    print('The number you entered is', number)
    
    # 