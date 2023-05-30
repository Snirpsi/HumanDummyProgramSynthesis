#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports and multiplyes words. """    
    ports = range(0,65535)
    words = ['word'] * len(ports)
    
    for port in ports:
        words[port] = 'port ' + str(port)
    
    print(words)
    
