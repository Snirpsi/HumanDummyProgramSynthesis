#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or prints all ports. """    
    ports = []
    while True:
        ports.append(int(input('Enter a port (1-65535): ')))
        if ports[-1] > 65535:
            ports.pop()
    
    ports.sort()
    for port in ports:
        print('Server listening on port ' + str(port))
    
