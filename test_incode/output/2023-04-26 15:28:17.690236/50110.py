#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers or converts all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        if port > 0:
            remove_ports(port)
        else:
            convert_ports()
    else:
        remove_ports()
        
