#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port. """    
    ports_to_remove = []
    while True:
        try:
            ports_to_remove.append(int(input('Enter a port to remove: ')))
        except ValueError:
            print('Invalid port')
            continue
        
        if ports_to_remove == []:
            print('No ports left to remove')
            continue
        
        print('Removing port', ports_to_remove[-1])
        
        remove_port(ports_to_remove[-1])
        
