#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input and returns all ports. """    
    ports = []
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        ports.append(int(port))
    print('\n'.join(map(str, ports)))
    
