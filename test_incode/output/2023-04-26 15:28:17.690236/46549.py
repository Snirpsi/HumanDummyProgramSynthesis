#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or converts numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        # User input
        
        number = int(sys.argv[1])
        
        # Convert numbers
        
        number = str(number)
        
        print(number)
        
    else:
        
        # User input
        
        number = int(input("Enter a number: "))
        
        # Convert numbers
        
        number = str(number)
        
        print(number)
        
