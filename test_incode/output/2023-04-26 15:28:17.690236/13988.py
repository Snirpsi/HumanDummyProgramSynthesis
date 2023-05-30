#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers or prints user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        # Print the user input
        print(sys.argv[1])
        
    else:
        
        # Print the user input
        print(input("Enter a number: "))
        
