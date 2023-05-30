#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports. """    
    
    ports_to_remove = []
    
    # Remove all ports except the one used by the webserver
    for port in range(80, 8080):
        ports_to_remove.append(port)
        
    for port in ports_to_remove:
        