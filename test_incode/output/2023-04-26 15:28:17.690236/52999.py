#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports and enumerates words. """    
    
    ports = range(5000, 5050)
    
    words = []
    for port in ports:
        words.append('Port {}'.format(port))
    
    for word in words:
        print('{} {}'.format(word, 