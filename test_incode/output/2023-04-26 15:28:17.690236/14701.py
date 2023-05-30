#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words or returns all ports. """    
    
    ports = convert_ports()
    
    if ports:
        print('\n'.join(ports))
    else:
        print('No ports found.')
    
    
