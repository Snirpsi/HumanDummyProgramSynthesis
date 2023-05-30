#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port or prints a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        if port > 0:
            remove_port(port)
        else:
            print_ports()
    else:
        print_ports()
        
