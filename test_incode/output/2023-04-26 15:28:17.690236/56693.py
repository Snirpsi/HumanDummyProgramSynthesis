#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and prints words. """    
    ports = []
    words = []
    
    for port in range(1, 65535):
        ports.append(port)
        
    for port in ports:
        words.append(port)
        
    for word in words:
        print('