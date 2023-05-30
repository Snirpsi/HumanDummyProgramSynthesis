#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports. """    
    
    # Read command line arguments
    args = sys.argv[1:]
    
    # Remove all ports
    remove_all_ports(args)
    
    # Print success
    print('All ports removed.')
    
