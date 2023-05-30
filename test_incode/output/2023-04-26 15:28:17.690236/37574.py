#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input and stores a list of numbers. """    
    while True:
        numbers = []
        
        # Read user input from the console
        numbers.append(int(input('Enter a number: ')))
        
        # Remove user input from the list
        numbers.remove(input('Enter a number: '))
        
        # Print the list
        print('The numbers are: ', numbers)
        
        # Wait for a keypress
        