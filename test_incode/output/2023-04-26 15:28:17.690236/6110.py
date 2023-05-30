#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words or opens all ports. """    
    ports = openPorts()
    
    for port in ports:
        print("Port: " + port)
        
