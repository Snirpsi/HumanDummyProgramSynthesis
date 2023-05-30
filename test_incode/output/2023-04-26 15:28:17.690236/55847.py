#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input or stores all ports. """    
    ports = []
    
    while True:
        ports.append(int(input('Enter a port number: ')))
    
    if len(ports) == 1:
        print('The port number is {0}'.format(ports[0]))
    else:
        print('The ports are: {0}'.format(ports))
        
