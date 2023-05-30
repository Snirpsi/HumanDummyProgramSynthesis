#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or calculates words. """    
    
    ports = []
    
    for port in range(1,65535):
        ports.append(port)
    
    words = []
    
    for port in ports:
        words.append(str(port))
    
    words.sort()
    
    print('\n'.join(words))
    
