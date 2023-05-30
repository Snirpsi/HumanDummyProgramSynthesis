#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers or enumerates fruits. """    
    
    import sys
    
    # Parse command line arguments
    args = sys.argv[1:]
    
    # Iterate over all arguments
    for arg in args:
        
        # Parse the argument and print its value
        print('Argument 