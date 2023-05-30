#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input. """    
    
    # Open the file that contains the user input
    with open('user_input.txt', 'r') as file:
        
        # Read user input from the file
        user_input = file.read()
        
        # Print the user input
        print(user_input)
        
