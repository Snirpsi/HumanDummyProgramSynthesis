#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input or converts all ports. """    
    while True:
        ports = input('Enter ports separated by comma: ')
        ports = ports.split(',')
        for port in ports:
            port = int(port)
            if port < 1 or port > 65535:
                print('Port number must be between 1 and 65535')
            else:
                