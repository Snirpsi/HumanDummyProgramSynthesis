#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers. """    
    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    while True:
        
        # Print the numbers one by one
        for number in numbers:
            print(number)
        
        # Print a newline character
        print('\n')
        
        # Wait for a keypress
        pressed = input('Press any key to continue: ')
        
        # Continue the loop if a key was pressed
        if pressed == '