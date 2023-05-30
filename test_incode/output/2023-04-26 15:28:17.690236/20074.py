#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words and enumerates a port. """    
    port = '/dev/ttyUSB0'
    
    words = remove_words(port)
    
    ports = enumerate_ports(words)
    
    print('\n'.join(ports))
    
