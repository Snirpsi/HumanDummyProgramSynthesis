#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints all ports and opens words. """    
    ports = openports()
    for port in ports:
        openport(port)
        
