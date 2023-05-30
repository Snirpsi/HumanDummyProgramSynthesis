#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds all ports or opens words. """    
    
    # Open the ports
    ports = openports()
    
    # Add all ports
    ports += openports()
    
    # Print the ports
    for port in ports:
        print(port)
    
    # Close the ports
    ports.close()
    
    # Close the program
    