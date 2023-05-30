#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns all ports or multiplyes a list of numbers. """    
    while True:
        port = input('Enter a port number: ')
        if port == 'q':
            break
        else:
            ports.append(int(port))
            
    for port in ports:
        print('The port number {} is {}'.format(port, port*2))
        
