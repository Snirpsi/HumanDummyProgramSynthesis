#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input or returns all ports. """    
    ports = []
    
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        ports.append(port)
    
    print('\n'.join(ports))
    
