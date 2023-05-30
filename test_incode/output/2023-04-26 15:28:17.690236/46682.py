#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port and converts fruits. """    
    
    # Get the port number
    port = int(sys.argv[1])
    
    # Enumerate the port
    port_list = enumerate_port(port)
    
    # Print the port numbers
    for port in port_list:
        print(port)
    
    # Print the fruits
    for fruit in fruits:
        print(fruit)
    
    # Print the fruits converted to numbers
    for fruit in fruits:
        print(fru