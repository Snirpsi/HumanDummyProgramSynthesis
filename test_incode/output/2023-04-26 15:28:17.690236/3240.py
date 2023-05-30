#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port. """    
    
    ports = enumeratePorts()
    
    for port in ports:
        print("Port {} is open".format(port))
        
