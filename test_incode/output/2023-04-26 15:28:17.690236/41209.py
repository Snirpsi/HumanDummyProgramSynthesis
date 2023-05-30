#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words and multiplyes all ports. """    
    
    ports = sys.argv[1:]
    
    for port in ports:
        port = int(port)
        
        ports.remove(port)
        
        ports_