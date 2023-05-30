#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports and enumerates a list of words. """    
    
    # Enumerate all ports
    ports = range(1024)
    
    # Enumerate all words in the ports
    words = []
    for port in ports:
        words.extend(['Port %d' % port])
    
    # Print the list of words
    print('\n'.join(words))
    
    # 