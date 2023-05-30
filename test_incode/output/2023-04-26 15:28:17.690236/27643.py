#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of numbers or multiplyes all ports. """    
    
    # Get the number of ports
    ports = int(sys.argv[1])
    
    # Get the list of ports
    ports_list = sys.argv[2:]
    
    # Get the list of ports
    ports_list = ports_list.split(",")
    
    # Get the list of ports
    ports_list = [int(p) for p in ports_list]
    
    # Get the list of ports
    ports_list = ports_list.