#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input. """    
    while True:
        
        # User input
        user_input = input('Enter a number: ')
        
        # Convert user input to int
        user_input = int(user_input)
        
        # Print the result
        print('The number you entered is', user_input)
        
        # Wait for user input
