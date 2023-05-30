#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a list of numbers or prints a port. """    
    ports = [int(i) for i in input().split()]
    
    if len(ports) == 1:
        print('Port: {}'.format(ports[0]))
    else:
        print('Ports: {}'.format(', '.join(str(i) for i in ports)))
        
