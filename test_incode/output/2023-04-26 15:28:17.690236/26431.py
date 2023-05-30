#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports. """    
    
    # Open all ports
    ports = openports()
    
    # Print the ports
    for port in ports:
        print(port)
    
    # Close all ports
    ports.close()

<|/ file source=github |>