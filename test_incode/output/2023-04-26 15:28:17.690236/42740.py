#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports and prints words. """    
    
    ports = enumeratePorts()
    for port in ports:
        print(port[0])
