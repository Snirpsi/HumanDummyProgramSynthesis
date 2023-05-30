#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds user input and returns all ports. """    
    ports = []
    while True:
        port = input('Enter a port number: ')
        if port == '':
            break
        ports.append(port)
    print('\n'.join(ports))
