#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port and stores fruits. """    
    
    ports_to_remove = []
    
    while True:
        ports_to_remove.append(input('Enter a port to remove: '))
        
        for port in ports_to_remove:
            
            