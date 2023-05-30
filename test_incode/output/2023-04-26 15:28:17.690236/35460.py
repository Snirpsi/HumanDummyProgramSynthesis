#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a port. """    
    
    ports = enumeratePorts()
    
    for port, desc in ports:
        print("{:<4}{:<20}".format(port, desc))
    
