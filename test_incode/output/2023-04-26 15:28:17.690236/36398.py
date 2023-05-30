#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of words or removes a port. """    
    
    # Read command line arguments
    args = sys.argv[1:]
    
    # Iterate over all arguments
    for arg in args:
        # Remove port from argument and print it
        print(arg.split(':')[0])
        
    # 