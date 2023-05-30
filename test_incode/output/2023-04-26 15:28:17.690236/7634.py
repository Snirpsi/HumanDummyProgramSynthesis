#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes fruits or calculates a port. """    
    
    # Read command line arguments
    args = sys.argv[1:]
    
    # Remove fruit
    if args.remove:
        remove_fruit()
    
    # Calculate port
    if args.port:
        calculate_port()
    
    # Exit program
    sys.exit()
    
