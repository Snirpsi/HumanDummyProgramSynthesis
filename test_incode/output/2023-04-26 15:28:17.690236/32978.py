#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes all ports and enumerates user input. """    
    
    # Get the port number
    port = int(input("Enter the port number: "))
    
    # Remove all ports
    remove_all_ports(port)
    
    # Enumerate user input
    enumerate_user_input(port)
    
    
