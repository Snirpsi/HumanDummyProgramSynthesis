#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or multiplyes a list of words. """    
    ports = []
    words = ['hello', 'world']
    
    for port in range(0, 65535):
        ports.append(port)
    
    for word in words:
        print('