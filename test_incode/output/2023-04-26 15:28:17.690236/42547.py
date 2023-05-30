#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or returns a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        # Print the list of numbers given
        numbers = sys.argv[1:]
        
        # Print the user input
        print(numbers)
        
    else:
        
        # Print the user input
        print(int(input('Enter a number: ')))
        
