#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports or multiplyes words. """    
    
    ports = range(65535)
    
    while True:
        word = ''
        for port in ports:
            word += str(port)
            
        print('