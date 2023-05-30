#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports and adds a list of words. """    
    
    ports = range(1024)
    
    while True:
        for port in ports:
            print(port)
            
