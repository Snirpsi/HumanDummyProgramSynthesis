#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and iterates over a list of numbers. """    
    
    port = int(sys.argv[1])
    
    ports_to_remove = []
    
    for port in range(port, 65535):
        ports_to_remove.append(port)
    
    for port in ports_to_remove:
        
        