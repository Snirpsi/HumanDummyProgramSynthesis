#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        # Read user input
        number = int(sys.argv[1])
        
        # Multiply numbers
        number *= 2
        
        # Print result
        print("The number is", number)
        
    else:
        print("Usage: python server.py <number>")
        
