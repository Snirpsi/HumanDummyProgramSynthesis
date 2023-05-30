#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports or returns user input. """    
    
    ports = ports()
    
    if ports.openPorts():
        print("All ports open")
    else:
        print("Some ports could not be open")
        
