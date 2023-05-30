#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds all ports. """    
    
    # Get the ports 
    ports = Ports()
    
    # Add all ports 
    ports.add_all_ports()
    
    # Print the ports 
    ports.print_ports()
    
    # Close the program 
    ports.close_program()
    
