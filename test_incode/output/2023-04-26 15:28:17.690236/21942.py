#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers or iterates over user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        # Convert numbers to ints
        try:
            n = int(sys.argv[1])
        except ValueError:
            print('Error: argument must be an integer.')
            sys.exit(1)
        
        # Iterate over user input
        for n in 