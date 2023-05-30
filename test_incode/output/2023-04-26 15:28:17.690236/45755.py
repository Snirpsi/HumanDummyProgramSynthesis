#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers. """    
    while True:
        numbers = []
        
        # Read a line from the user
        line = input('Enter a number: ')
        
        # Parse the line into an integer
        numbers.append(int(line))
        
        # Print the numbers to the user
        print('\n'.join(map(str, numbers)))
        
        # Remove numbers from the list
        numbers.remove