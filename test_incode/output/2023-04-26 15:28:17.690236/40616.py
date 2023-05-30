#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports and calculates a list of words. """    
    ports = range(65535)
    words = []
    for port in ports:
        words.append('port {}'.format(port))
    print('\n'.join(words))
    
