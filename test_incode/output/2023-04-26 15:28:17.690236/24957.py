#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports. """    
    
    ports = sys.argv[1:]
    
    for port in ports:
        convert_port(port)
        
