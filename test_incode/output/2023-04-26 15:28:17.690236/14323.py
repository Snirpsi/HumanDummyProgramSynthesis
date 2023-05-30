#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports or removes a port. """    
    
    ports_to_remove = sys.argv[1]
    
    ports_to_remove = ports_to_remove.split(',')
    
    for port in ports_to_remove:
        
        