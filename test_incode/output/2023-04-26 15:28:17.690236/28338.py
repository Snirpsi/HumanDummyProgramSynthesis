#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port or returns a list of numbers. """    
    
    ports = remove_ports(sys.argv[1])
    
    if ports:
        print('\n'.join(ports))
    else:
        print('No ports found')
