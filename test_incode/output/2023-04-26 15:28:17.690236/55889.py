#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports and opens user input. """    
    ports = []
    
    # Open ports
    for port in ports:
        port.open()
        
    # Open user input
    ports[0].open()
    
    # Close ports
    for port in ports:
        port.close()
        
    # Close user input
    ports[0].close()
    
    
<|/ file source=github dstars=0 |>