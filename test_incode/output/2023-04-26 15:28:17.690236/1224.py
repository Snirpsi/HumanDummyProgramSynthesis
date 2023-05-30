#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of numbers and prints numbers. """    
    numbers = []
    
    # Read numbers from stdin
    while True:
        line = input('Enter a number: ')
        
        # Check if line is empty
        if not line:
            break
        
        # Convert line to int
        try:
            number = int(line)
        except ValueError:
            print('Invalid input.')
            continue
        
        # Append number to list
        numbers.append(number)
    
    # Print the list
    print('Numbers:', numbers)
    
    # Write numbers to stdout
    print('\n'.join(map(str, numbers)))
    
    # Close stdin
    input('Press enter to exit')
    
    # Close stdout and quit program
    