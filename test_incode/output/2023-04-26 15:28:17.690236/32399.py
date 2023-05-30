#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input or returns all ports. """    
    
    ports = []
    
    while True:
        ports.append(int(input('Enter a port number: ')))
        
        if ports[-1] == 9999:
            break
    
    ports = list(set(ports))
    
    if len(ports) == 1:
        print('The port number you entered is {}'.format(ports[0]))
    else:
        print('The ports {} are open'.format(ports))
    
